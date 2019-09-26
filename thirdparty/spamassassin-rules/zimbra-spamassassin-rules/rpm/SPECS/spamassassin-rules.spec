Summary:            Default ruleset for SpamAssassin
Name:               zimbra-spamassassin-rules
Version:            1.0.0
Release:            alt1
License:            Apache-2.0
Requires:           zimbra-mta-base, zimbra-perl-mail-spamassassin
Packager:           Evgeniy Korneechev <ekorneechev@altlinux.org>
Group:              Development/Languages
AutoReqProv:        no

%define debug_package %{nil}

%description
Default ruleset for SpamAssassin

%install
mkdir -p ${RPM_BUILD_ROOT}/opt/zimbra/data/spamassassin/rules
cp ../../../rules/updates_spamassassin_org/* ${RPM_BUILD_ROOT}/opt/zimbra/data/spamassassin/rules/

%files
%defattr(-,zimbra,zimbra)
/opt/zimbra/data/spamassassin/rules

%changelog
* Wed Sep 25 2019 Evgeniy Korneechev <ekorneechev@altlinux.org> 1.0.0-alt1
- Initial build for p8

