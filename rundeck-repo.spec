name: rundeck-repo
version: 5
release: 1
summary: Rundeck Repository Bootstrap
group: Applications/System
license: APL
packager: greg AT simplifyops DOT com
requires: yum

%description
This package contains the necessary yum .repo files that can be used to bootstrap the repository configuration for installing Rundeck.

%files
/etc/yum.repos.d/rundeck.repo
