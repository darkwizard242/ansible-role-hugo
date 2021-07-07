[![build-test](https://github.com/darkwizard242/ansible-role-hugo/workflows/build-and-test/badge.svg?branch=master)](https://github.com/darkwizard242/ansible-role-hugo/actions?query=workflow%3Abuild-and-test) [![release](https://github.com/darkwizard242/ansible-role-hugo/workflows/release/badge.svg)](https://github.com/darkwizard242/ansible-role-hugo/actions?query=workflow%3Arelease) ![Ansible Role](https://img.shields.io/ansible/role/47495?color=dark%20green%20) ![Ansible Role](https://img.shields.io/ansible/role/d/47495?label=role%20downloads) ![Ansible Quality Score](https://img.shields.io/ansible/quality/47495?label=ansible%20quality%20score) [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-hugo&metric=alert_status)](https://sonarcloud.io/dashboard?id=ansible-role-hugo) [![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-hugo&metric=sqale_rating)](https://sonarcloud.io/dashboard?id=ansible-role-hugo) [![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-hugo&metric=reliability_rating)](https://sonarcloud.io/dashboard?id=ansible-role-hugo) [![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-hugo&metric=security_rating)](https://sonarcloud.io/dashboard?id=ansible-role-hugo) ![GitHub tag (latest SemVer)](https://img.shields.io/github/tag/darkwizard242/ansible-role-hugo?label=release) ![GitHub repo size](https://img.shields.io/github/repo-size/darkwizard242/ansible-role-hugo?color=orange&style=flat-square)

# Ansible Role: Hugo

Role to install (_by default_) extended [hugo](https://github.com/gohugoio/hugo) on **Debian/Ubuntu** and **EL** systems.

## Requirements

None.

## Role Variables

Available variables are listed below (located in `defaults/main.yml`):

### Variables list:

```yaml
hugo_app: hugo_extended
hugo_version: 0.85.0
hugo_osarch: {{ ansible_system }}-64bit
hugo_dl_url: https://github.com/gohugoio/hugo/releases/download/v{{ hugo_version }}/{{ hugo_app }}_{{ hugo_version }}_{{ hugo_osarch }}.tar.gz
hugo_bin_path: /usr/local/bin
```

### Variables table:

Variable      | Value (default)                                                                                                                     | Description
------------- | ----------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------
hugo_app      | hugo_extended                                                                                                                       | Defines the app to install i.e. **hugo_extended**
hugo_version  | 0.85.0                                                                                                                              | Defined to dynamically fetch the desired version to install. Defaults to: **0.85.0**
hugo_osarch   | {{ ansible_system }}-64bit                                                                                                          | Defines os architecture. Used for obtaining the correct type of binaries based on OS System Architecture. Defaults to: **{{ ansible_system }}-64bit**
hugo_dl_url   | <https://github.com/gohugoio/hugo/releases/download/v{{> hugo_version }}/{{ hugo_app }}_{{ hugo_version }}_{{ hugo_osarch }}.tar.gz | Defines URL to download the hugo binary from.
hugo_bin_path | /usr/local/bin                                                                                                                      | Defined to dynamically set the appropriate path to store hugo binary into. Defaults to (as generally available on any user's PATH): **/usr/local/bin**

## Dependencies

None

## Example Playbook

For default behaviour of role (i.e. installation of **hugo**) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.hugo
```

For customizing behavior of role (i.e. specifying the desired **hugo** version) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.hugo
  vars:
    hugo_version: 0.78.2
```

For customizing behavior of role (i.e. placing binary of **hugo** package in different location) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.hugo
  vars:
    hugo_bin_path: /bin/
```

## License

[MIT](https://github.com/darkwizard242/ansible-role-hugo/blob/master/LICENSE)

## Author Information

This role was created by [Ali Muhammad](https://www.linkedin.com/in/ali-muhammad-759791130/).
