# packages
ZCS Third Party Dependency Build System

This is the official repository for building out the third party dependencies for Zimbra Collaboration Suite 8.7 and later.

To build the packages in this repository please checkout the following repositories:

  - packages            git@github.com:ekorneechev/packages.git
  - zimbra-build        git@github.com:ekorneechev/zm-build.git
  - zimbra-package-stub git@github.com:ekorneechev/zimbra-package-stub.git

Перед сборкой данных пакетов необходимо развернуть локальный репозиторий для собранных пакетов (лучше сразу [FTP](https://www.altlinux.org/Настройка_FTP): /var/ftp/local, пригодится для последующей установки).

BuildRequires:
    
    perl-Test-Inter perl-CPAN perl-Module-Build perl-Test-TrailingSpace \
    perl-Test-Pod perl-Test-Pod-Coverage perl-XML-SAX perl-Test-Deep perl-DBM perl-PlRPC \
    perl-Socket6 perl-Encode-JP perl-Tk perl-Test-Warn libmagic-devel libidn-devel libncurses-devel \
    libexpat-devel zlib-devel bzip2-devel pcre-devel libnl-devel librpm-devel libsensors3-devel \
    libwrap-devel pdksh python-module-setuptools chrpath libcheck-devel libcurl-devel libssl-devel \
    libxml2-devel graphviz groff-extra gv doxygen flex mercurial  libX11-devel libXau-devel \
    libXext-devel libXfixes-devel libXtst-devel libXi-devel libxcb-devel xorg-xproto-devel \
    libICE-devel libSM-devel libXt-devel libXrender-devel libkeyutils-devel libselinux-devel \
    libsepol-devel cups-devel libfreetype-devel libalsa-devel java-1.7.0-openjdk-devel \
    cmake-2.8.10 libaio-devel glibc-devel-static libssh2-devel libnghttp2-devel

For MariaDB:

    ln -s /usr/include/pcre/pcre.h /usr/include/pcre.h
    ln -s /usr/include/pcre/pcreposix.h /usr/include/pcreposix.h

0. Необходим bash 4ой версии, рекомендуется sudo без пароля для пользователя.
1. Сборка базовых пакетов zimbra-*-core:

       ./make_zimbra.sh
       
2. Проверка готовности:

       cd zimbra ; ./check_build.sh
       > 22
       > Need:
       > 23
3. Запускаем копирование собранных пакетов в локальный репозиторий:

       cd .. ; sudo ./update.sh
4. Далее снова запускаем сборку, вполне возможно требования уже будут выполнены (или нужны пакеты thirdparty).
5. После успешной сборки всех пакетов в папке zimbra, собираем (так же рекурсивно) пакеты thirdparty

       make_perl.sh; sudo ./update.sh
       make_3dparty.sh; sudo ./update.sh
       cd thirdparty; ./check_build.sh
