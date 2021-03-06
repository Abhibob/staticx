# Change Log
All notable changes to this project will be documented in this file.
This project adheres to [Semantic Versioning](http://semver.org/).

## [Unreleased]
### Changed
- Improved tar extraction to minimize number of write() calls ([#131])

### Fixed
- Bundled applications retain their original name ([#135])


## [0.10.0] - 2020-05-30
### Added
- Added `sx-extract` archive extraction/dumping tool ([#114])

### Removed
- Drop support for Python 2.7 ([#115])


## [0.9.1] - 2020-01-29
### Fixed
- Correct handling of absolute path symlink in ldd output ([#118])
- Fixed null tmpdir argument error on GCC9 ([#120])
- Fixed ldd "you do not have execution permission..." warning ([#122])


## [0.9.0] - 2020-01-11
### Added
- Staticx binaries now respect `$TMPDIR` for creating temporary directory ([#101])

### Changed
- Ensure user program is always marked executable in archive ([#112])

### Fixed
- Don't hard-code exclusion of `linux-vdso.so.1` ([#102])

### Removed
- Drop support for Python 3.4 ([#111])


## [0.8.1] - 2019-12-30
### Changed
- Changed `setup.py` to respect `BOOTLOADER_CC`, to simplify `.travis.yml` and
  ensure that released wheels are always built with musl-libc.

## [0.8.0] - 2019-12-30
### Added
- Set `STATICX_BUNDLE_DIR` and `STATICX_PROG_PATH` in child process ([#81])
- Add `--debug` flag to bundle debug bootloader ([#87])

### Changed
- Changed pyinstaller hook to ignore static executables ([#83])

### Fixed
- Always generate tar archive in GNU format. Python 3.8 changed the default to
  PAX which is not supported by our libtar. ([#85])
- Add backports.lzma to setup.py for Python 2, removing manual requirement ([#89])

## [0.7.0] - 2019-03-10
### Changed
- Refactored and trimmed libtar ([#74])

### Fixed
- Correctly handle applications and libraries that specify an `RPATH` including
  `$ORIGIN`, including apps built with PyInstaller ([#75])
- Fixed potential issue in ignored libraries list ([#77])
- Fixed missing libxz in source distributions ([#77])


## [0.6.0] - 2018-11-13
### Added
- Add `--no-compress` option to store archive uncompressed ([#58])

### Changed
- Detect if user app is a different machine type than the bootloader ([#56])
- Drop support for Python 3.2 and 3.3 ([#65])

### Fixed
- Use `<sys/sysmacros.h>` for makedev() ([#63])
- Handle subdirectories when extracting Pyinstaller archives ([#69])
- Handle shared objects with no dependencies ([#70])


## [0.5.0] - 2017-07-16
### Added
- Added `--strip` option to strip binaries while adding to archive ([#39])

### Changed
- Raise error if given output path is a directory ([#52])
- Dynamically select XZ BCJ filter ([#54])


## [0.4.1] - 2017-07-15
### Fixed
- Fixes for release builds deployed to PyPI

## [0.4.0] - 2017-07-13
### Added
- Compress archive with LZMA (plus x86 BCJ filter) ([#46])


## [0.3.2] - 2017-06-15
### Fixed
- Fixed PyPI bdists not including bootloader ([#32])


## [0.3.1] - 2017-06-14
### Fixed
- Work around `FTW_MOUNT` bug in musl<1.0.0 ([#30])


## [0.3.0] - 2017-06-13
### Added
- Auto-detect additional dependencies for apps built with PyInstaller ([#21])

### Changed
- Compatibility fixes for older versions of Python and GCC
- Handle multiple levels of library symlinks ([#18])


## [0.2.0] - 2017-05-31
### Changed
- Work on temporary file while building application ([#12])
- Run user application in child process to enable cleanup ([#9])


## 0.1.0 - 2017-05-30
Initial release


[Unreleased]: https://github.com/JonathonReinhart/staticx/compare/v0.10.0...HEAD
[0.10.0]: https://github.com/JonathonReinhart/staticx/compare/v0.9.1...v0.10.0
[0.9.1]: https://github.com/JonathonReinhart/staticx/compare/v0.9.0...v0.9.1
[0.9.0]: https://github.com/JonathonReinhart/staticx/compare/v0.8.1...v0.9.0
[0.8.1]: https://github.com/JonathonReinhart/staticx/compare/v0.8.0...v0.8.1
[0.8.0]: https://github.com/JonathonReinhart/staticx/compare/v0.7.0...v0.8.0
[0.7.0]: https://github.com/JonathonReinhart/staticx/compare/v0.6.0...v0.7.0
[0.6.0]: https://github.com/JonathonReinhart/staticx/compare/v0.5.0...v0.6.0
[0.5.0]: https://github.com/JonathonReinhart/staticx/compare/v0.4.1...v0.5.0
[0.4.1]: https://github.com/JonathonReinhart/staticx/compare/v0.4.0...v0.4.1
[0.4.0]: https://github.com/JonathonReinhart/staticx/compare/v0.3.2...v0.4.0
[0.3.2]: https://github.com/JonathonReinhart/staticx/compare/v0.3.1...v0.3.2
[0.3.1]: https://github.com/JonathonReinhart/staticx/compare/v0.3.0...v0.3.1
[0.3.0]: https://github.com/JonathonReinhart/staticx/compare/v0.2.0...v0.3.0
[0.2.0]: https://github.com/JonathonReinhart/staticx/compare/v0.1.0...v0.2.0

[#9]: https://github.com/JonathonReinhart/staticx/pull/9
[#12]: https://github.com/JonathonReinhart/staticx/pull/12
[#18]: https://github.com/JonathonReinhart/staticx/pull/18
[#21]: https://github.com/JonathonReinhart/staticx/pull/21
[#30]: https://github.com/JonathonReinhart/staticx/pull/30
[#32]: https://github.com/JonathonReinhart/staticx/pull/32
[#39]: https://github.com/JonathonReinhart/staticx/pull/39
[#46]: https://github.com/JonathonReinhart/staticx/pull/46
[#52]: https://github.com/JonathonReinhart/staticx/pull/52
[#54]: https://github.com/JonathonReinhart/staticx/pull/54
[#56]: https://github.com/JonathonReinhart/staticx/pull/56
[#58]: https://github.com/JonathonReinhart/staticx/pull/58
[#63]: https://github.com/JonathonReinhart/staticx/pull/63
[#65]: https://github.com/JonathonReinhart/staticx/pull/65
[#69]: https://github.com/JonathonReinhart/staticx/pull/69
[#70]: https://github.com/JonathonReinhart/staticx/pull/70
[#74]: https://github.com/JonathonReinhart/staticx/pull/74
[#75]: https://github.com/JonathonReinhart/staticx/pull/75
[#77]: https://github.com/JonathonReinhart/staticx/pull/77
[#81]: https://github.com/JonathonReinhart/staticx/pull/81
[#83]: https://github.com/JonathonReinhart/staticx/pull/83
[#85]: https://github.com/JonathonReinhart/staticx/pull/85
[#87]: https://github.com/JonathonReinhart/staticx/pull/87
[#89]: https://github.com/JonathonReinhart/staticx/pull/89
[#101]: https://github.com/JonathonReinhart/staticx/pull/101
[#102]: https://github.com/JonathonReinhart/staticx/pull/102
[#111]: https://github.com/JonathonReinhart/staticx/pull/111
[#112]: https://github.com/JonathonReinhart/staticx/pull/112
[#114]: https://github.com/JonathonReinhart/staticx/pull/114
[#115]: https://github.com/JonathonReinhart/staticx/pull/115
[#118]: https://github.com/JonathonReinhart/staticx/pull/118
[#120]: https://github.com/JonathonReinhart/staticx/pull/120
[#122]: https://github.com/JonathonReinhart/staticx/pull/122
[#131]: https://github.com/JonathonReinhart/staticx/pull/131
[#135]: https://github.com/JonathonReinhart/staticx/pull/135
