Summary:            Zimbra components for MTA package
Name:               zimbra-mta-components
Version:            1.0.4
Release:            alt1.zimbra884
License:            GPL-2
Requires:           sqlite, zimbra-mta-base, zimbra-altermime, zimbra-amavisd
Requires:           zimbra-clamav, zimbra-clamav-db, zimbra-cluebringer, zimbra-mariadb >= 10.1.25-alt1.zimbra884
Requires:           zimbra-opendkim, zimbra-perl-mail-spamassassin >= 3.4.1-alt1.zimbra884, zimbra-postfix
Requires:           zimbra-spamassassin-rules
Packager:           Korneechev Evgeniy <ekorneechev@altlinux.org>
Group:              Development/Languages
AutoReqProv:        no

%define debug_package %{nil}

%description
Zimbra mta components pulls in all the packages used by
zimbra-mta

%changelog
* Mon Jul 24 2017  Zimbra Packaging Services <packaging-devel@zimbra.com> - 1.0.4
- Updated zimbra-mariadb package
* Tue Jul 18 2017  Zimbra Packaging Services <packaging-devel@zimbra.com> - 1.0.3
- Updated zimbra-perl-mail-spamassassin package
* Wed Mar 09 2016  Zimbra Packaging Services <packaging-devel@zimbra.com> - 1.0.2
- Add ClamAV initial databases
* Fri Dec 14 2015  Zimbra Packaging Services <packaging-devel@zimbra.com> - 1.0.1
- Add Spamassassin default ruleset

%files
