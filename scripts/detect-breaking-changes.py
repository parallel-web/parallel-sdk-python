from __future__ import annotations

import sys
from typing import Iterator
from pathlib import Path

import rich
import griffe
from rich.text import Text
from rich.style import Style


def _resolve_redirect(obj: griffe.Object | griffe.Alias) -> griffe.Object | griffe.Alias | None:
    """Follow back-compat redirections to a real class definition.

    We use two patterns to preserve import paths after a schema rename:
      * `from .new_path import NewClass` → `griffe.Alias`
      * `OldName = NewClass` (module-level assignment) → `griffe.Attribute`
    Both are runtime-equivalent re-exports and should expose the target
    class's attributes for breaking-change detection. Without resolving them,
    griffe reports every old attribute as removed.
    """
    visited: set[int] = set()
    current: griffe.Object | griffe.Alias = obj
    while id(current) not in visited:
        visited.add(id(current))
        if isinstance(current, griffe.Alias):
            try:
                final = current.final_target
            except Exception:
                return None
            if final is current:
                return None
            return final
        if isinstance(current, griffe.Attribute):
            value = current.value
            parent = current.parent
            if parent is None or value is None:
                return None
            if isinstance(value, griffe.ExprName):
                next_obj = parent.members.get(str(value))
                if next_obj is None:
                    return None
                current = next_obj
                continue
            if isinstance(value, griffe.ExprAttribute):
                # Qualified path like `task_group_status.TaskGroupStatus`.
                # Walk segment by segment, resolving any module aliases as we go.
                next_obj: griffe.Object | griffe.Alias | None = parent
                for segment in value.values:
                    if not isinstance(segment, griffe.ExprName):
                        continue
                    if isinstance(next_obj, griffe.Alias):
                        try:
                            next_obj = next_obj.final_target
                        except Exception:
                            return None
                    if next_obj is None or not hasattr(next_obj, "members"):
                        return None
                    next_obj = next_obj.members.get(str(segment))
                if next_obj is None:
                    return None
                current = next_obj
                continue
            return None
        return current
    return None


def public_members(obj: griffe.Object | griffe.Alias) -> dict[str, griffe.Object | griffe.Alias]:
    target = _resolve_redirect(obj)
    if target is not None and target is not obj:
        obj = target

    if isinstance(obj, griffe.Alias):
        # Truly opaque alias we couldn't resolve.
        return {}

    return {name: value for name, value in obj.all_members.items() if not name.startswith("_")}


def find_breaking_changes(
    new_obj: griffe.Object | griffe.Alias,
    old_obj: griffe.Object | griffe.Alias,
    *,
    path: list[str],
) -> Iterator[Text | str]:
    new_members = public_members(new_obj)
    old_members = public_members(old_obj)

    for name, old_member in old_members.items():
        if isinstance(old_member, griffe.Alias) and len(path) > 2:
            # ignore imports in `/types/` for now, they're technically part of the public API
            # but we don't have good preventative measures in place to prevent changing them
            continue

        new_member = new_members.get(name)
        if new_member is None:
            cls_name = old_member.__class__.__name__
            yield Text(f"({cls_name})", style=Style(color="rgb(119, 119, 119)"))
            yield from [" " for _ in range(10 - len(cls_name))]
            yield f" {'.'.join(path)}.{name}"
            yield "\n"
            continue

        yield from find_breaking_changes(new_member, old_member, path=[*path, name])


def main() -> None:
    try:
        against_ref = sys.argv[1]
    except IndexError as err:
        raise RuntimeError("You must specify a base ref to run breaking change detection against") from err

    package = griffe.load(
        "parallel",
        search_paths=[Path(__file__).parent.parent.joinpath("src")],
    )
    old_package = griffe.load_git(
        "parallel",
        ref=against_ref,
        search_paths=["src"],
    )
    assert isinstance(package, griffe.Module)
    assert isinstance(old_package, griffe.Module)

    output = list(find_breaking_changes(package, old_package, path=["parallel"]))
    if output:
        rich.print(Text("Breaking changes detected!", style=Style(color="rgb(165, 79, 87)")))
        rich.print()

        for text in output:
            rich.print(text, end="")

        sys.exit(1)


main()
