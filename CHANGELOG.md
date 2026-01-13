# Changelog

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
