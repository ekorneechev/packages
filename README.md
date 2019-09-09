# packages
ZCS Third Party Dependency Build System

This is the official repository for building out the third party dependencies for Zimbra Collaboration Suite 8.7 and later.

To build the packages in this repository please checkout the following repositories:

  - packages            git@github.com:ekorneechev/packages.git
  - zimbra-build        git@github.com:ekorneechev/zm-build.git
  - zimbra-package-stub git@github.com:ekorneechev/zimbra-package-stub.git

Перед сборкой данных пакетов необходимо развернуть локальный репозиторий для собранных пакетов (лучше сразу [FTP](https://www.altlinux.org/Настройка_FTP): /var/ftp/local, пригодится для последующей установки). 

0. Необходим bash 4ой версии, рекомендуется sudo без пароля для пользователя.
1. Сборка базовых пакетов zimbra-*-core:

       $ ./make_zimbra.sh
       
2. Проверка готовности:

       $ cd zimbra ; ./check_build.sh
       22
       Need:
       24
3. Запускаем копирование собранных пакетов в локальный репозиторий:

       $ cd .. ; sudo ./update.sh
4. Далее снова запускаем сборку, вполне возможно требования уже будут выполнены.
5. После успешной сборки всех пакетов в папке zimbra, собираем (так же рекурсивно) пакеты thirdparty

       $ make_perl.sh; sudo ./update.sh
       $ make_3dparty.sh; sudo ./update.sh
       $ cd thirdparty; ./check_build.sh
