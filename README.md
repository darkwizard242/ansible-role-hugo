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
hugo_version: 0.123.7
hugo_os: "{{ ansible_system }}"
hugo_arch: "64bit"
hugo_dl_url: https://github.com/gohugoio/hugo/releases/download/v{{ hugo_version }}/{{ hugo_app }}_{{ hugo_version }}_{{ hugo_os }}-{{ hugo_arch }}.tar.gz
hugo_bin_path: /usr/local/bin
hugo_file_owner: root
hugo_file_group: root
hugo_file_mode: '0755'
```

### Variables table:

Variable        | Description
--------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------
hugo_app        | Defines the app to install i.e. **hugo_extended**
hugo_version    | Defined to dynamically fetch the desired version to install. Defaults to: **0.123.7**
hugo_os         | Defines OS type. Used for obtaining the correct type of binaries based on OS. Defaults to: **{{ ansible_system }}**
hugo_arch       | Defines Architecture type. Used for obtaining the correct type of binaries based on Architecture. Defaults to: **64bit**
hugo_dl_url     | Defines URL to download the hugo binary from.
hugo_bin_path   | Defined to dynamically set the appropriate path to store hugo binary into. Defaults to (as generally available on any user's PATH): **/usr/local/bin**
hugo_file_owner | Owner for the binary file of hugo.
hugo_file_group | Group for the binary file of hugo.
hugo_file_mode  | Mode for the binary file of hugo.

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

This role was created by [Ali Muhammad](https://www.alimuhammad.dev/).
