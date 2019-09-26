Summary:            Zimbra Perl Base
Name:               zimbra-perl-base
Version:            1.0.0
Release:            alt1
License:            GPL-2
Packager:           Evgeniy Korneechev <ekorneechev@altlinux.org>
Group:              Development/Languages
BuildRequires:      perl
Requires:           perl, zimbra-base
AutoReqProv:        no

%define debug_package %{nil}

%description
Zimbra Perl Base is used as a simple method to allow removing
all the zimbra specific perl modules.  It in itself has no
actual contents.

%files

%changelog
* Wed Sep 25 2019 Evgeniy Korneechev <ekorneechev@altlinux.org> 1.0.0-alt1
- Initial build for p8

