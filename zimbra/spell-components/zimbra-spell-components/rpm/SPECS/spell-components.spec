Summary:            Zimbra components for spell package
Name:               zimbra-spell-components
Version:            1.0.1
Release:            alt1.zimbra8.8.15
License:            GPL-2
Requires:           zimbra-spell-base, zimbra-aspell-ar, zimbra-aspell-da, zimbra-aspell-de
Requires:           zimbra-aspell-en, zimbra-aspell-es, zimbra-aspell-fr, zimbra-aspell-hi
Requires:           zimbra-aspell-hu, zimbra-aspell-it, zimbra-aspell-nl, zimbra-aspell-pl
Requires:           zimbra-aspell-pt-br, zimbra-aspell-ru, zimbra-aspell-sv, zimbra-httpd,
Requires:           zimbra-php >= 5.6.31-alt1.zimbra8.8.15, zimbra-aspell-zimbra
Packager:           Korneechev Evgeniy <ekorneechev@altlinux.org>
Group:              Development/Languages
AutoReqProv:        no

%define debug_package %{nil}

%description
Zimbra spell components pulls in all the packages used by
zimbra-spell

%changelog
* Fri Jul 28 2017  Zimbra Packaging Services <packaging-devel@zimbra.com> - 1.0.1
- Updated PHP package.
* Wed Sep 09 2015 Zimbra Packaging Services <packaging-devel@zimbra.com> - 1.0.0
- Inital release

%files
