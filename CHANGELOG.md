# Changelog

## 1.1.0 (2026-06-08)

Full Changelog: [v1.0.1...v1.1.0](https://github.com/parallel-web/parallel-sdk-python/compare/v1.0.1...v1.1.0)

### Features

* **api:** add turbo mode to search ([8ee340d](https://github.com/parallel-web/parallel-sdk-python/commit/8ee340d76c4af67c15371b3d786aa870f14ded9e))

## 1.0.1 (2026-06-03)

Full Changelog: [v1.0.0...v1.0.1](https://github.com/parallel-web/parallel-sdk-python/compare/v1.0.0...v1.0.1)

### Chores

* remove undocumented backwards-compat alias shims ([e5a2ad8](https://github.com/parallel-web/parallel-sdk-python/commit/e5a2ad80cdd6e4f708c3ec05c9df8b8ede79a772))
* **types:** drop redundant NotRequired on task_spec input_schema ([b356c22](https://github.com/parallel-web/parallel-sdk-python/commit/b356c22e718ab1a95a40b6b37917a5b8bcbb091a))


### Documentation

* regenerate api.md from spec (drop hand-maintained patch) ([05d2897](https://github.com/parallel-web/parallel-sdk-python/commit/05d28970ff8b3efc77b1c4ef60beecc654a52385))
* regenerate README from spec (drop hand-maintained patch) ([c7ed169](https://github.com/parallel-web/parallel-sdk-python/commit/c7ed169c66a60485b309147fb7aa1b6d2e551766))

## 1.0.0 (2026-06-02)

Full Changelog: [v0.6.0...v1.0.0](https://github.com/parallel-web/parallel-sdk-python/compare/v0.6.0...v1.0.0)

### ⚠ BREAKING CHANGES

* **api:** clean up beta features

### Features

* **api:** 1.0.0 changes ([f399080](https://github.com/parallel-web/parallel-sdk-python/commit/f3990800a98eefef82f21902406d90073c050de1))
* **api:** Add parallel_beta typing back ([004ce9f](https://github.com/parallel-web/parallel-sdk-python/commit/004ce9f53eaabe12e676f9f6ae3d0a000dfeabc2))
* **api:** clean up beta features ([f533161](https://github.com/parallel-web/parallel-sdk-python/commit/f53316197d11be2900710b447007c07f9c89e427))
* **api:** Remove beta: tasks, task groups, search, and extract from SDK ([b7bcade](https://github.com/parallel-web/parallel-sdk-python/commit/b7bcade5a866ea8ef08de244b251c140b17f18f2))
* **internal/types:** support eagerly validating pydantic iterators ([6c148b4](https://github.com/parallel-web/parallel-sdk-python/commit/6c148b449af221b634c8dd77c3846401c2d092b8))


### Bug Fixes

* **client:** add missing f-string prefix in file type error message ([6fa3eac](https://github.com/parallel-web/parallel-sdk-python/commit/6fa3eaca98c7d94d0a98596227ab2f10968cea86))

## 0.6.0 (2026-05-06)

Full Changelog: [v0.5.1...v0.6.0](https://github.com/parallel-web/parallel-sdk-python/compare/v0.5.1...v0.6.0)

### Features

* **api:** manual updates ([8cb17ac](https://github.com/parallel-web/parallel-sdk-python/commit/8cb17ac6d6c9a5a9e6443d9ecf5c121250b2eed2))
* **api:** manual updates ([e4008e4](https://github.com/parallel-web/parallel-sdk-python/commit/e4008e4f8432a6c3e2341d18fee37fcedf8a530e))
* **api:** manual updates ([174407f](https://github.com/parallel-web/parallel-sdk-python/commit/174407ff7467789e19d3abeffcaccd36fd35e786))
* **api:** manual updates ([1c47c8b](https://github.com/parallel-web/parallel-sdk-python/commit/1c47c8baa579a403064e59a5fbb75400315951c9))
* **api:** Task Groups v1 added to SDK ([198e317](https://github.com/parallel-web/parallel-sdk-python/commit/198e317bb3b5e5961e63c1c04bac0eb593385b7b))
* support setting headers via env ([6dd2b05](https://github.com/parallel-web/parallel-sdk-python/commit/6dd2b05bcf25259ae50e650376c3182913439487))


### Bug Fixes

* re-export TaskGroup from parallel.types.beta and silence reportDeprecated ([dc6119f](https://github.com/parallel-web/parallel-sdk-python/commit/dc6119f6dccdef75bdbe4ce838dd8ba51cc2428a))
* **scripts:** remove unreachable check and redundant type annotation ([f63ad0a](https://github.com/parallel-web/parallel-sdk-python/commit/f63ad0ae48994be8b16c20438bb80c61cd943fec))
* **scripts:** satisfy pyright in alias resolver ([892f474](https://github.com/parallel-web/parallel-sdk-python/commit/892f4743488ae5d8c4683123193da4f4e61d2464))
* **types:** preserve back-compat aliases for renamed inline classes ([532ee8f](https://github.com/parallel-web/parallel-sdk-python/commit/532ee8f32ecbaf611f0ff5f6c80a532e2f0bcd66))
* **types:** use module-level alias instead of import-as ([b1b9858](https://github.com/parallel-web/parallel-sdk-python/commit/b1b9858ffa95d90871ce36b06e510638e3546bde))
* use correct field name format for multipart file arrays ([1e34228](https://github.com/parallel-web/parallel-sdk-python/commit/1e3422859a25c66804f7f588fd24276417c52057))


### Chores

* **internal:** more robust bootstrap script ([d4c7737](https://github.com/parallel-web/parallel-sdk-python/commit/d4c773762e983a657fb4c6f5d39529c3467e0994))
* **internal:** reformat pyproject.toml ([b3c0639](https://github.com/parallel-web/parallel-sdk-python/commit/b3c063982542886a490679f840ca0fad94695227))
* **scripts:** follow alias and attribute redirections in breaking-change detection ([89b1495](https://github.com/parallel-web/parallel-sdk-python/commit/89b1495236f280eee8af7c48ecff3ff2453291bd))
* stop tracking uv.lock (project uses requirements*.lock from rye) ([540471a](https://github.com/parallel-web/parallel-sdk-python/commit/540471afb4da3a6ed485af15554cb548e7086bbd))

## 0.5.1 (2026-04-22)

Full Changelog: [v0.5.0...v0.5.1](https://github.com/parallel-web/parallel-sdk-python/compare/v0.5.0...v0.5.1)

### Features

* **api:** manual updates ([86c7d33](https://github.com/parallel-web/parallel-sdk-python/commit/86c7d334df7c2018d0277fe3efa93fb7029f6a41))
* **api:** Mark search and extract as deprecated ([cfdea3b](https://github.com/parallel-web/parallel-sdk-python/commit/cfdea3b19622911e65c9359f0acdbd4b201d2d08))
* **api:** OpenAPI changes ([cfc5fb3](https://github.com/parallel-web/parallel-sdk-python/commit/cfc5fb373a46c73c2f79057b593712d7b847ee33))

## 0.5.0 (2026-04-21)

Full Changelog: [v0.4.2...v0.5.0](https://github.com/parallel-web/parallel-sdk-python/compare/v0.4.2...v0.5.0)

### Features

* **api:** Add Findall Candidates ([57c4ae2](https://github.com/parallel-web/parallel-sdk-python/commit/57c4ae25d77a8627c6be3673312bfd7f373e17da))
* **api:** Add Search and Extract v1 and associated types ([ea487f3](https://github.com/parallel-web/parallel-sdk-python/commit/ea487f32b73aee955f662d1fa225841421ce1ba3))
* **api:** manual - add AdvancedSearchSettings and AdvancedExtractSettings models ([5836a6f](https://github.com/parallel-web/parallel-sdk-python/commit/5836a6fbe8db3a3509556442067f087918edb2bb))
* **api:** manual updates - update openapi spec ([02db6c0](https://github.com/parallel-web/parallel-sdk-python/commit/02db6c07ec5eb254b18732fcb6f7dc43e31de471))
* **api:** Remove full_content from OpenAPI Spec ([7a4d651](https://github.com/parallel-web/parallel-sdk-python/commit/7a4d651c3e9f35334175f82daaf6392e9f76dee5))
* **api:** Search/Extract v1 with advanced_settings and max_results ([4ded29c](https://github.com/parallel-web/parallel-sdk-python/commit/4ded29c2382594f1735101753a0b09a2f7c6972e))
* **api:** Update OpenAPI spec ([58f19f3](https://github.com/parallel-web/parallel-sdk-python/commit/58f19f38174fb71dc906049c0aef6610ac67971e))
* **api:** Update OpenAPI spec ([fae95f4](https://github.com/parallel-web/parallel-sdk-python/commit/fae95f4f2c7cb60ebc0babc4fe540617e3334b2d))
* **internal:** implement indices array format for query and form serialization ([3df5972](https://github.com/parallel-web/parallel-sdk-python/commit/3df5972e34c9aa1709eabc4eb5b8cbbc0adccae2))


### Bug Fixes

* **client:** preserve hardcoded query params when merging with user params ([08080bc](https://github.com/parallel-web/parallel-sdk-python/commit/08080bc22c415881cc9f9b05bc22f09ab83c7e8d))
* **deps:** bump minimum typing-extensions version ([964a46d](https://github.com/parallel-web/parallel-sdk-python/commit/964a46ddfc9ead64e4105e42192a780bc91716b0))
* ensure file data are only sent as 1 parameter ([1c15cc0](https://github.com/parallel-web/parallel-sdk-python/commit/1c15cc00b1ae223db8e51893ce23b9a2193e3ae7))
* **pydantic:** do not pass `by_alias` unless set ([f0793c1](https://github.com/parallel-web/parallel-sdk-python/commit/f0793c171465dd57d0fbf82a3bb2281d046f500e))
* sanitize endpoint path params ([5931597](https://github.com/parallel-web/parallel-sdk-python/commit/59315972d27246485be5cb52671aecaa3aa46253))


### Performance Improvements

* **client:** optimize file structure copying in multipart requests ([00e8564](https://github.com/parallel-web/parallel-sdk-python/commit/00e856464a2828693483a704de83ee5d6c4fe19e))


### Chores

* **ci:** skip lint on metadata-only changes ([403448c](https://github.com/parallel-web/parallel-sdk-python/commit/403448c7760e70fe0f4b3998a20f048910e91cd6))
* **internal:** tweak CI branches ([014c802](https://github.com/parallel-web/parallel-sdk-python/commit/014c80287318df0db6207df1579be00c4717f24d))
* **internal:** update gitignore ([1f4f6b0](https://github.com/parallel-web/parallel-sdk-python/commit/1f4f6b0e5d2a46e1a5457879e937ea5aa551073c))
* **tests:** bump steady to v0.19.4 ([ebee2e7](https://github.com/parallel-web/parallel-sdk-python/commit/ebee2e761e2a8587cc6aa4c2decfd6310092b039))
* **tests:** bump steady to v0.19.5 ([2774099](https://github.com/parallel-web/parallel-sdk-python/commit/2774099f753bc0826e9c6b6e9fbb40d4e72e3405))
* **tests:** bump steady to v0.19.6 ([8e3ee3d](https://github.com/parallel-web/parallel-sdk-python/commit/8e3ee3d04dc149b2bcedb0e4acd92474fafd8d05))
* **tests:** bump steady to v0.19.7 ([4bcf12e](https://github.com/parallel-web/parallel-sdk-python/commit/4bcf12e670b7997e23ade3d991711fe1ef741e35))
* **tests:** bump steady to v0.20.1 ([d82ce60](https://github.com/parallel-web/parallel-sdk-python/commit/d82ce601c5687553b0e96990e418289fd8a14e00))
* **tests:** bump steady to v0.20.2 ([746ca39](https://github.com/parallel-web/parallel-sdk-python/commit/746ca39c749f899dc9137a2f9be5de9aa39210c6))
* **tests:** bump steady to v0.22.1 ([dec81af](https://github.com/parallel-web/parallel-sdk-python/commit/dec81afb89f46850635daa89e64debe15717d053))


### Refactors

* **tests:** switch from prism to steady ([032745e](https://github.com/parallel-web/parallel-sdk-python/commit/032745ea1a03b3d2516b789a28a3c8b8034660d8))

## 0.4.2 (2026-03-09)

Full Changelog: [v0.4.1...v0.4.2](https://github.com/parallel-web/parallel-sdk-python/compare/v0.4.1...v0.4.2)

### Features

* **api:** add betas back in for search ([23493c6](https://github.com/parallel-web/parallel-sdk-python/commit/23493c6ae666649f7ac2af185bb6caf49b9fefee))
* **api:** sync openapi spec ([e00288b](https://github.com/parallel-web/parallel-sdk-python/commit/e00288bd8ed2a250c9a0d7935a52fd40b9d1bec5))
* **client:** add custom JSON encoder for extended type support ([b2c8bf9](https://github.com/parallel-web/parallel-sdk-python/commit/b2c8bf9b8246e2e8f1d53a7c8e238dd19b727a77))


### Chores

* **ci:** skip uploading artifacts on stainless-internal branches ([bb389c0](https://github.com/parallel-web/parallel-sdk-python/commit/bb389c0078e00e615c1aa650674c006c6e906c81))
* format all `api.md` files ([b74b93b](https://github.com/parallel-web/parallel-sdk-python/commit/b74b93bf04d678cc283b8f312a3a4c5bb314c468))
* **internal:** add request options to SSE classes ([00dbc30](https://github.com/parallel-web/parallel-sdk-python/commit/00dbc3027e59adda51eb623d6a724501f70a7720))
* **internal:** bump dependencies ([f49c841](https://github.com/parallel-web/parallel-sdk-python/commit/f49c841670d88f8fc38e0a17f19242f7570a9aad))
* **internal:** codegen related update ([1b7c8ff](https://github.com/parallel-web/parallel-sdk-python/commit/1b7c8ff1969c65a422d6bcfcdc01c5b0c477b45b))
* **internal:** fix lint error on Python 3.14 ([cb3f364](https://github.com/parallel-web/parallel-sdk-python/commit/cb3f3645bc67b98235a732f357d8a24fdf164032))
* **internal:** make `test_proxy_environment_variables` more resilient ([d3ba149](https://github.com/parallel-web/parallel-sdk-python/commit/d3ba149917deab7ee28a3f38bd7b1f3f4bd2b9c6))
* **internal:** make `test_proxy_environment_variables` more resilient to env ([1e1d858](https://github.com/parallel-web/parallel-sdk-python/commit/1e1d858e7c21785744d94ceef33e655dcf75eacc))
* **test:** do not count install time for mock server timeout ([9766097](https://github.com/parallel-web/parallel-sdk-python/commit/9766097052cc86f0081cfe38b25d7dbf90232438))
* update mock server docs ([028965c](https://github.com/parallel-web/parallel-sdk-python/commit/028965c0b2868051617b266493466f9fc7816705))

## 0.4.1 (2026-01-28)

Full Changelog: [v0.4.0...v0.4.1](https://github.com/parallel-web/parallel-sdk-python/compare/v0.4.0...v0.4.1)

### Features

* **client:** add support for binary request streaming ([1138841](https://github.com/parallel-web/parallel-sdk-python/commit/1138841ae071ae81665158a2407d36502524b8a6))


### Chores

* **api:** make headers optional ([f99b59d](https://github.com/parallel-web/parallel-sdk-python/commit/f99b59d1ebd829a2c3c62a9a814941f6299f3653))
* **ci:** upgrade `actions/github-script` ([293c778](https://github.com/parallel-web/parallel-sdk-python/commit/293c778ea739104cc0f153bc099515b5d0d4d339))
* **internal:** update `actions/checkout` version ([326daf2](https://github.com/parallel-web/parallel-sdk-python/commit/326daf24e43d2a45e077d435db63d72187039207))

## 0.4.0 (2026-01-13)

Full Changelog: [v0.3.4...v0.4.0](https://github.com/parallel-web/parallel-sdk-python/compare/v0.3.4...v0.4.0)

### Features

* **api:** add after_date, update findAll nomenclature ([3641ac6](https://github.com/parallel-web/parallel-sdk-python/commit/3641ac619abdf3f0acd9085c515f3bed19c9bdd2))
* **api:** Update excerpt settings ([bafa464](https://github.com/parallel-web/parallel-sdk-python/commit/bafa464c3f124690387410b0d17bf8a1253e8e63))


### Bug Fixes

* ensure streams are always closed ([3251033](https://github.com/parallel-web/parallel-sdk-python/commit/325103322362df0fe730362841dbc0d4b3a60c18))
* **types:** allow pyright to infer TypedDict types within SequenceNotStr ([f134f9b](https://github.com/parallel-web/parallel-sdk-python/commit/f134f9bf488bdcd80088fc7752b5d33d84fcca66))
* use async_to_httpx_files in patch method ([b147da5](https://github.com/parallel-web/parallel-sdk-python/commit/b147da50e3d4b13868908c5c40e0ddecc5489e19))


### Chores

* add missing docstrings ([05118fc](https://github.com/parallel-web/parallel-sdk-python/commit/05118fc081e6907ac0cdde365e5ed364f49b769c))
* add Python 3.14 classifier and testing ([5588224](https://github.com/parallel-web/parallel-sdk-python/commit/558822483f60eb430a795e0ee5c6ac780c5f56c1))
* **api:** update default headers ([16949bf](https://github.com/parallel-web/parallel-sdk-python/commit/16949bfab087cf2f6e6e4f2dc3a503a4a7fa285f))
* **deps:** mypy 1.18.1 has a regression, pin to 1.17 ([e327c6e](https://github.com/parallel-web/parallel-sdk-python/commit/e327c6e2ba27b3dd565c3f36537643889b4c43e8))
* **docs:** use environment variables for authentication in code snippets ([e44bc95](https://github.com/parallel-web/parallel-sdk-python/commit/e44bc9528e5e16f243aa8dee4633730d2899c72d))
* **internal:** add `--fix` argument to lint script ([8b25ed1](https://github.com/parallel-web/parallel-sdk-python/commit/8b25ed10edef5697bce6bc74a3f628029da28d12))
* **internal:** add missing files argument to base client ([9bc7dc6](https://github.com/parallel-web/parallel-sdk-python/commit/9bc7dc653a4f75da0c5af3297170a16b1df91875))
* **internal:** codegen related update ([2eb1adc](https://github.com/parallel-web/parallel-sdk-python/commit/2eb1adc9884c03202107eb5987b6ea0717dd3a6a))
* speedup initial import ([2927603](https://github.com/parallel-web/parallel-sdk-python/commit/2927603782bc242da5b6d7622963452dd24154e7))
* update lockfile ([37bb7a6](https://github.com/parallel-web/parallel-sdk-python/commit/37bb7a6d321646946f52d37455fc5ad1a2458154))

## 0.3.4 (2025-11-12)

Full Changelog: [v0.3.3...v0.3.4](https://github.com/parallel-web/parallel-sdk-python/compare/v0.3.3...v0.3.4)

### Features

* **api:** FindAll sdk updates ([e07fd1e](https://github.com/parallel-web/parallel-sdk-python/commit/e07fd1e75f5562f471454d5ab4d7ecb4334f42ad))
* **api:** manual updates ([f9957bf](https://github.com/parallel-web/parallel-sdk-python/commit/f9957bf3721b8efe0138c8f8bd96a929419087a1))


### Bug Fixes

* compat with Python 3.14 ([a63f4ee](https://github.com/parallel-web/parallel-sdk-python/commit/a63f4eeeb7d7193765d4dbcac1781e67615a5580))
* **compat:** update signatures of `model_dump` and `model_dump_json` for Pydantic v1 ([cf9de5f](https://github.com/parallel-web/parallel-sdk-python/commit/cf9de5f7a8c1f6e026c441b24aad6e5712d7845b))


### Chores

* **package:** drop Python 3.8 support ([ba0bf24](https://github.com/parallel-web/parallel-sdk-python/commit/ba0bf24b6476e341fc497a70e6fdfb890b0923a4))

## 0.3.3 (2025-11-06)

Full Changelog: [v0.3.2...v0.3.3](https://github.com/parallel-web/parallel-sdk-python/compare/v0.3.2...v0.3.3)

### Features

* **api:** add fetch_policy and mode to /v1beta/search ([1d7200a](https://github.com/parallel-web/parallel-sdk-python/commit/1d7200a56264719ea109e352c3ef0a02609495fd))


### Bug Fixes

* **api:** add back /v1/tasks/runs?=beta ([bdecee5](https://github.com/parallel-web/parallel-sdk-python/commit/bdecee5bfd3811751c340ef4ac38e76cdf264c29))
* **api:** Make beta headers optional in /v1beta/extract ([bc9e1c2](https://github.com/parallel-web/parallel-sdk-python/commit/bc9e1c205267203806d09cf52c0a30482fff40b8))
* **api:** re-add deprecated max_chars_per_result ([e0976a1](https://github.com/parallel-web/parallel-sdk-python/commit/e0976a12f85f88c82d40ee8129963c483d53cf3b))
* **api:** re-add deprecated processor to /v1beta/extract ([d656151](https://github.com/parallel-web/parallel-sdk-python/commit/d6561513ed508f4337b650269090c55eea00d7f9))
* **api:** remove full_content from /v1beta/search output ([c13d6db](https://github.com/parallel-web/parallel-sdk-python/commit/c13d6db25c054a91d0a4c0fa0ad09c051cf0a92a))
* **client:** close streams without requiring full consumption ([e6ba5dc](https://github.com/parallel-web/parallel-sdk-python/commit/e6ba5dc8bb4cc3ad283540e46375e799e5a10cea))


### Chores

* **internal/tests:** avoid race condition with implicit client cleanup ([4ec359d](https://github.com/parallel-web/parallel-sdk-python/commit/4ec359dbc78ec6bf64780fcf7499d684205442a8))
* **internal:** grammar fix (it's -&gt; its) ([fd8a351](https://github.com/parallel-web/parallel-sdk-python/commit/fd8a3518051b452c6e9aff121592c67f60e1be13))
* **lint:** reorder imports ([901e4f1](https://github.com/parallel-web/parallel-sdk-python/commit/901e4f1a5597a662764ce9d4a890d3075f484984))

## 0.3.2 (2025-10-22)

Full Changelog: [v0.3.1...v0.3.2](https://github.com/parallel-web/parallel-sdk-python/compare/v0.3.1...v0.3.2)

### Bug Fixes

* **api:** default beta headers for v1beta/search and v1beta/extract ([9f8d8dd](https://github.com/parallel-web/parallel-sdk-python/commit/9f8d8dd6e40f77fb0d1eaf6cc300cb853e734cdf))

## 0.3.1 (2025-10-21)

Full Changelog: [v0.3.0...v0.3.1](https://github.com/parallel-web/parallel-sdk-python/compare/v0.3.0...v0.3.1)

### Features

* **api:** manual updates ([0acbe77](https://github.com/parallel-web/parallel-sdk-python/commit/0acbe77da0148029c21e6b3c541e0b1ca163038d))

## 0.3.0 (2025-10-21)

Full Changelog: [v0.2.2...v0.3.0](https://github.com/parallel-web/parallel-sdk-python/compare/v0.2.2...v0.3.0)

### Features

* **api:** Add /v1beta/extract ([df40ff5](https://github.com/parallel-web/parallel-sdk-python/commit/df40ff551e5a5e91576066de4c8216e3bd7e1bb1))


### Chores

* bump `httpx-aiohttp` version to 0.1.9 ([4da4812](https://github.com/parallel-web/parallel-sdk-python/commit/4da4812c00f76d6613eb14b388b84171ceee074d))

## 0.2.2 (2025-10-16)

Full Changelog: [v0.2.1...v0.2.2](https://github.com/parallel-web/parallel-sdk-python/compare/v0.2.1...v0.2.2)

### Features

* **api:** Add progress meter to Task Run events ([176f9d3](https://github.com/parallel-web/parallel-sdk-python/commit/176f9d318d9d9367b61e40fb6f8c27576e75deb4))


### Bug Fixes

* do not set headers with default to omit ([8989f91](https://github.com/parallel-web/parallel-sdk-python/commit/8989f9120217bba2c95b2b256a2767f885311652))


### Chores

* do not install brew dependencies in ./scripts/bootstrap by default ([c3250e2](https://github.com/parallel-web/parallel-sdk-python/commit/c3250e26311cc9b767d06a112317b74f73f78644))
* **internal:** detect missing future annotations with ruff ([db5980c](https://github.com/parallel-web/parallel-sdk-python/commit/db5980ce6d58ac926eea60d836b36dc8bdd651d7))
* **internal:** update pydantic dependency ([96f50db](https://github.com/parallel-web/parallel-sdk-python/commit/96f50dbffc919f591a149f89b387ebf19bd4deb0))
* **types:** change optional parameter type from NotGiven to Omit ([0f0fa20](https://github.com/parallel-web/parallel-sdk-python/commit/0f0fa20994ddb2c89d0def2a16a68b9499e1abd4))

## 0.2.1 (2025-09-15)

Full Changelog: [v0.2.0...v0.2.1](https://github.com/parallel-web/parallel-sdk-python/compare/v0.2.0...v0.2.1)

### Features

* **api:** Allow nullable text schemas ([dc87604](https://github.com/parallel-web/parallel-sdk-python/commit/dc87604a3c83bf7c30086c4c23c4e689628bc5a7))
* improve future compat with pydantic v3 ([ea49f26](https://github.com/parallel-web/parallel-sdk-python/commit/ea49f26543681aa59de34577cae1fb8a57b077c5))
* **types:** replace List[str] with SequenceNotStr in params ([6155c3f](https://github.com/parallel-web/parallel-sdk-python/commit/6155c3f30b46ce9bd39aaadc3dddf275d555e2ba))


### Chores

* **internal:** codegen related update ([72ec907](https://github.com/parallel-web/parallel-sdk-python/commit/72ec90723bac0b80a9c8e79f7cab985425beedad))
* **internal:** move mypy configurations to `pyproject.toml` file ([e03d641](https://github.com/parallel-web/parallel-sdk-python/commit/e03d64154278ebd8d844751d4d55e275177cf4f1))
* **tests:** simplify `get_platform` test ([9862221](https://github.com/parallel-web/parallel-sdk-python/commit/9862221997402f105c75df206004fc8d6e206ce8))

## 0.2.0 (2025-09-01)

Full Changelog: [v0.1.3...v0.2.0](https://github.com/parallel-web/parallel-sdk-python/compare/v0.1.3...v0.2.0)

### Features

* **api:** update via SDK Studio ([b048bd7](https://github.com/parallel-web/parallel-sdk-python/commit/b048bd7e1c5a992ae274aa4b6df16a9d5b0f843e))
* **api:** update via SDK Studio ([b9abf3c](https://github.com/parallel-web/parallel-sdk-python/commit/b9abf3c8b0e22b260149f01b1ef608924eefe735))
* **api:** update via SDK Studio ([4326698](https://github.com/parallel-web/parallel-sdk-python/commit/43266988c2123fa1aff00bf0b62c355b0c2bf04e))
* clean up environment call outs ([3a102e9](https://github.com/parallel-web/parallel-sdk-python/commit/3a102e9a05476e4d28c0ac386cd156cc0fe8b5cf))
* **client:** add support for aiohttp ([4e2aa32](https://github.com/parallel-web/parallel-sdk-python/commit/4e2aa32ad8242745f56e5a8b810d33c362967dad))
* **client:** support file upload requests ([ec0c2cf](https://github.com/parallel-web/parallel-sdk-python/commit/ec0c2cf30bd24524567232ad0f661facda124203))


### Bug Fixes

* add types for backwards compatibility ([c975302](https://github.com/parallel-web/parallel-sdk-python/commit/c975302c0d61d1d6731ccaeb7977c2009cb0b666))
* avoid newer type syntax ([2ea196d](https://github.com/parallel-web/parallel-sdk-python/commit/2ea196d5d4c7881e61dc848a1387770b4e27e304))
* **ci:** correct conditional ([99d37f6](https://github.com/parallel-web/parallel-sdk-python/commit/99d37f657a249987ccae60dd0e62f296ab0c1d85))
* **ci:** release-doctor — report correct token name ([310076b](https://github.com/parallel-web/parallel-sdk-python/commit/310076b2f8a75ed29ba2a1fae0f6e840ec43bb5b))
* **client:** don't send Content-Type header on GET requests ([f103b4a](https://github.com/parallel-web/parallel-sdk-python/commit/f103b4a72fc25f6a8dd1bda0c8d040aba1f527d1))
* **parsing:** correctly handle nested discriminated unions ([c9a2300](https://github.com/parallel-web/parallel-sdk-python/commit/c9a23002be2d78a11b5c1b7c901f4ddb32663393))
* **parsing:** ignore empty metadata ([ab434aa](https://github.com/parallel-web/parallel-sdk-python/commit/ab434aa7bd088fc16279255ae36138ab6dff0730))
* **parsing:** parse extra field types ([85f5cd4](https://github.com/parallel-web/parallel-sdk-python/commit/85f5cd4191ae168ed443e78a2c7bd747d51404b3))


### Chores

* **ci:** change upload type ([40dbd3b](https://github.com/parallel-web/parallel-sdk-python/commit/40dbd3b7d5becf0fe54b62a4acd8696957380053))
* **ci:** only run for pushes and fork pull requests ([d55fbea](https://github.com/parallel-web/parallel-sdk-python/commit/d55fbea54037d2d833ecc281cbddbc8d6700d24d))
* **internal:** add Sequence related utils ([cb9a7a9](https://github.com/parallel-web/parallel-sdk-python/commit/cb9a7a905ca4a4a9ba35e540f6c47a8bf89c87d2))
* **internal:** bump pinned h11 dep ([818f1dd](https://github.com/parallel-web/parallel-sdk-python/commit/818f1ddb3ba1be6bfdb9aee1322d6a3d8a98667a))
* **internal:** change ci workflow machines ([a90da34](https://github.com/parallel-web/parallel-sdk-python/commit/a90da34910585453eac918a5f273749c00d2f743))
* **internal:** codegen related update ([47ea68b](https://github.com/parallel-web/parallel-sdk-python/commit/47ea68bd44ad52ac1c18e7215c013f408914890c))
* **internal:** fix ruff target version ([4e5dbda](https://github.com/parallel-web/parallel-sdk-python/commit/4e5dbda03907f45ac31d18d89714e86f26e79866))
* **internal:** update comment in script ([631b045](https://github.com/parallel-web/parallel-sdk-python/commit/631b045ae2f138e4c8098fafd9466451d61ca82a))
* **internal:** update pyright exclude list ([8d2fb29](https://github.com/parallel-web/parallel-sdk-python/commit/8d2fb29b5d80a2fa9ee81a6f9510134fb7bab908))
* **internal:** version bump ([90d26a5](https://github.com/parallel-web/parallel-sdk-python/commit/90d26a5e8db8bd6a27f9bbc96595da87bd7ea0f3))
* **package:** mark python 3.13 as supported ([6fa54c4](https://github.com/parallel-web/parallel-sdk-python/commit/6fa54c42a17f5e731f5e97214f0212a0828d3cb8))
* **project:** add settings file for vscode ([acdeda2](https://github.com/parallel-web/parallel-sdk-python/commit/acdeda2f1f95f5bade2da52d5a2aa8560e71369d))
* **readme:** fix version rendering on pypi ([2bf10b0](https://github.com/parallel-web/parallel-sdk-python/commit/2bf10b073ab7e015b08c106d265a9091752df51a))
* **readme:** Remove references to methods, update FAQ for beta ([cefefbf](https://github.com/parallel-web/parallel-sdk-python/commit/cefefbfccba78fdabcc925728836d70400d4e5aa))
* **tests:** skip some failing tests on the latest python versions ([13b1533](https://github.com/parallel-web/parallel-sdk-python/commit/13b153381e9b7c998a7ebef878518222678dfa83))
* update @stainless-api/prism-cli to v5.15.0 ([56b5aab](https://github.com/parallel-web/parallel-sdk-python/commit/56b5aab87a833c27b8e1a2bc7c4bf2169ee281a8))
* update github action ([3d90e19](https://github.com/parallel-web/parallel-sdk-python/commit/3d90e196184e540242fb310cc55b0219d20dff45))

## 0.1.3 (2025-08-09)

Full Changelog: [v0.1.2...v0.1.3](https://github.com/parallel-web/parallel-sdk-python/compare/v0.1.2...v0.1.3)

### Chores

* **readme:** update descriptions ([3212a0f](https://github.com/parallel-web/parallel-sdk-python/commit/3212a0fc32d744e7df3d0dcedf527b176a73a91b))

## 0.1.2 (2025-06-25)

Full Changelog: [v0.1.1...v0.1.2](https://github.com/parallel-web/parallel-sdk-python/compare/v0.1.1...v0.1.2)

### Features

* **api:** add execute method and structured output support ([5e51379](https://github.com/parallel-web/parallel-sdk-python/commit/5e51379e3ff28bdf70a3cc9167d4413bf3e8690c))
* **api:** update via SDK Studio ([7526908](https://github.com/parallel-web/parallel-sdk-python/commit/752690867c75ee970582fabc05c939a2f619cb3f))
* **api:** update via SDK Studio ([6698e71](https://github.com/parallel-web/parallel-sdk-python/commit/6698e716bdddcf2146cc802cfaaa26f7ddb4d3dc))
* **client:** add follow_redirects request option ([deff733](https://github.com/parallel-web/parallel-sdk-python/commit/deff733f189070bb471ebd6cbf92dfd61d19734a))


### Bug Fixes

* **api:** handle retryable errors ([#2](https://github.com/parallel-web/parallel-sdk-python/issues/2)) ([5317550](https://github.com/parallel-web/parallel-sdk-python/commit/531755070eb4b798a7f0b51153414425a0c293b0))
* **client:** correctly parse binary response | stream ([9546f27](https://github.com/parallel-web/parallel-sdk-python/commit/9546f276ca2d63cf3c6a9b0eef23f1eed35758fa))
* **package:** support direct resource imports ([52fe297](https://github.com/parallel-web/parallel-sdk-python/commit/52fe297a34a6a2a473be0f124e2febab1df527fe))
* **pydantic:** add fields to json schema, better error messages ([38a2ddc](https://github.com/parallel-web/parallel-sdk-python/commit/38a2ddc348ac7acf11f9f75f69900b628e539c1d))
* **tests:** fix: tests which call HTTP endpoints directly with the example parameters ([bfad009](https://github.com/parallel-web/parallel-sdk-python/commit/bfad009314f4f3ce31265d2be07f091eb7db664a))


### Chores

* **ci:** enable for pull requests ([0ae47ea](https://github.com/parallel-web/parallel-sdk-python/commit/0ae47eaf080510a886eb40aed7c8189faa940f2c))
* **ci:** fix installation instructions ([150a642](https://github.com/parallel-web/parallel-sdk-python/commit/150a6429ee584a0c32160be88d9bdcd4eeab4579))
* **ci:** upload sdks to package manager ([3bd8b36](https://github.com/parallel-web/parallel-sdk-python/commit/3bd8b361b84bad87c0943c2fe71465c92cdea599))
* **docs:** grammar improvements ([c5b636b](https://github.com/parallel-web/parallel-sdk-python/commit/c5b636bfeb60b02f84f5b9e93687359cd9c5c251))
* **docs:** remove reference to rye shell ([a64869e](https://github.com/parallel-web/parallel-sdk-python/commit/a64869e70e9c493f2dc3e8618327f28544d36058))
* **docs:** remove unnecessary param examples ([e15712a](https://github.com/parallel-web/parallel-sdk-python/commit/e15712a074ba66a6b0d225bb3a6979a767c15225))
* **internal:** avoid errors for isinstance checks on proxies ([4149fb9](https://github.com/parallel-web/parallel-sdk-python/commit/4149fb963b39db2211f404f94bf7b55a57c2556b))
* **internal:** codegen related update ([6a0bb66](https://github.com/parallel-web/parallel-sdk-python/commit/6a0bb662f5011bbea13f75334eb55c5144b50e8b))
* **internal:** update conftest.py ([0e08356](https://github.com/parallel-web/parallel-sdk-python/commit/0e0835661e91993042605131065729d006761a5a))
* **readme:** update badges ([36c14b5](https://github.com/parallel-web/parallel-sdk-python/commit/36c14b529ec8611508b6b7cc9065c67e59e5ecdc))
* **readme:** update low level api examples ([f17e34e](https://github.com/parallel-web/parallel-sdk-python/commit/f17e34e0e0a6d3205c344c278f1643826938e9d1))
* **tests:** add tests for httpx client instantiation & proxies ([d84ffff](https://github.com/parallel-web/parallel-sdk-python/commit/d84ffff48a814edc81ef62249353053df6398c90))
* **tests:** run tests in parallel ([62252c6](https://github.com/parallel-web/parallel-sdk-python/commit/62252c6f1098ad138978b6efa1fc2a9c22961040))


### Documentation

* **client:** fix httpx.Timeout documentation reference ([17f87ee](https://github.com/parallel-web/parallel-sdk-python/commit/17f87eef5af2b06b3791f9218b7ab4f9098faf9c))

## 0.1.1 (2025-04-25)

Full Changelog: [v0.1.0...v0.1.1](https://github.com/shapleyai/parallel-sdk-python/compare/v0.1.0...v0.1.1)

### Features

* **api:** update via SDK Studio ([4cc79c4](https://github.com/shapleyai/parallel-sdk-python/commit/4cc79c4d1edaa9d1d080b81830961252c8b327c1))


### Bug Fixes

* **pydantic:** add fields to json schema, better error messages ([38a2ddc](https://github.com/shapleyai/parallel-sdk-python/commit/38a2ddc348ac7acf11f9f75f69900b628e539c1d))


### Chores

* **readme:** update low level api examples ([f17e34e](https://github.com/shapleyai/parallel-sdk-python/commit/f17e34e0e0a6d3205c344c278f1643826938e9d1))

## 0.1.0 (2025-04-24)

Full Changelog: [v0.0.1-alpha.0...v0.1.0](https://github.com/shapleyai/parallel-sdk-python/compare/v0.0.1-alpha.0...v0.1.0)

### Features

* **api:** add execute method and structured output support ([5e51379](https://github.com/shapleyai/parallel-sdk-python/commit/5e51379e3ff28bdf70a3cc9167d4413bf3e8690c))
* **api:** update via SDK Studio ([c393d04](https://github.com/shapleyai/parallel-sdk-python/commit/c393d048bddb554c37eb750ca57c4335243a70ed))
* **api:** update via SDK Studio ([6698e71](https://github.com/shapleyai/parallel-sdk-python/commit/6698e716bdddcf2146cc802cfaaa26f7ddb4d3dc))


### Chores

* go live ([061677a](https://github.com/shapleyai/parallel-sdk-python/commit/061677a22549f3dd3d9f4591c9ccfdf71209c12e))
