Summary:            Mozilla's CA cert bundle in PEM format
Name:               zimbra-perl-mozilla-ca
Version:            VERSION
Release:            alt1
License:            MPL-2
Source:             %{name}-%{version}.tar.gz
Packager:           Evgeniy Korneechev <ekorneechev@altlinux.org>
Group:              Development/Languages
BuildRequires:      zimbra-perl-base
Requires:           zimbra-perl-base
AutoReqProv:        no
URL:                https://metacpan.org/release/Mozilla-CA

%description
Mozilla::CA provides a copy of Mozilla's bundle of Certificate Authority certificates
in a form that can be consumed by modules and libraries based on OpenSSL.

%define debug_package %{nil}

%prep
%setup -n Mozilla-CA-%{version}

%build
perl -I OZCL/perl5 Makefile.PL INSTALL_BASE=OZC \
 INSTALLSITEMAN1DIR=OZCS/man/man1 INSTALLSITEMAN3DIR=OZCS/man/man3 \
 LIB=OZCL/perl5
make test

# remove .packlist and perllocal.pod
#  $(DESTINSTALLSITEARCH)/auto/$(FULLEXT)/.packlist
#  $(DESTINSTALLSITEARCH)/perllocal.pod
%define perl_archname %(perl -MConfig -e 'print $Config{archname}')
%install
make install DESTDIR=${RPM_BUILD_ROOT}
rm -rf %{buildroot}OZCL/perl5/%{perl_archname}

%files
%defattr(-,root,root)
OZCL
OZCS/man

%changelog
* Wed Sep 25 2019 Evgeniy Korneechev <ekorneechev@altlinux.org> VERSION-alt1
- Initial build for p8

