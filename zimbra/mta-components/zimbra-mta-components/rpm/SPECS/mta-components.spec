Summary:            Zimbra components for MTA package
Name:               zimbra-mta-components
Version:            1.0.5
Release:            alt1
License:            GPL-2
Requires:           sqlite, zimbra-mta-base, zimbra-altermime, zimbra-amavisd
Requires:           zimbra-clamav, zimbra-clamav-db, zimbra-cluebringer, zimbra-mariadb
Requires:           zimbra-opendkim, zimbra-perl-mail-spamassassin, zimbra-postfix
Requires:           zimbra-spamassassin-rules
Packager:           Evgeniy Korneechev <ekorneechev@altlinux.org>
Group:              Development/Languages
AutoReqProv:        no

%define debug_package %{nil}

%description
Zimbra mta components pulls in all the packages used by
zimbra-mta

%changelog
* Wed Sep 25 2019 Evgeniy Korneechev <ekorneechev@altlinux.org> 1.0.5-alt1
- Initial build for p8


%files
