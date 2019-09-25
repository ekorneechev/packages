Summary:            LWP::Protocol::https - Provide https support for LWP::UserAgent 
Name:               zimbra-perl-lwp-protocol-https
Version:            VERSION
Release:            alt1.zimbra8.8.15
License:            GPL+ or Artistic
Source:             %{name}-%{version}.tar.gz
Packager:           Korneechev Evgeniy <ekorneechev@altlinux.org>
Group:              Development/Languages
BuildRequires:      zimbra-perl-base, zimbra-perl-libwww, zimbra-perl-net-http
BuildRequires:      zimbra-perl-io-socket-ssl, zimbra-perl-mozilla-ca
Requires:           zimbra-perl-base, zimbra-perl-libwww, zimbra-perl-net-http
Requires:           zimbra-perl-io-socket-ssl, zimbra-perl-mozilla-ca
AutoReqProv:        no
URL:                https://metacpan.org/release/LWP-Protocol-https

%description
The LWP::Protocol::https module provides support for using https schemed
URLs with LWP. This module is a plug-in to the LWP protocol handling, so
you don't use it directly. Once the module is installed LWP is able to
access sites using HTTP over SSL/TLS.

%define debug_package %{nil}

%prep
%setup -n LWP-Protocol-https-%{version}

%build
perl -I OZCL/perl5 Makefile.PL INSTALL_BASE=OZC \
 INSTALLSITEMAN1DIR=OZCS/man/man1 INSTALLSITEMAN3DIR=OZCS/man/man3 \
 INSTALLMAN1DIR=OZCS/man/man1 INSTALLVENDORMAN1DIR=OZCS/man/man1 \
 INSTALLMAN3DIR=OZCS/man/man3 INSTALLVENDORMAN3DIR=OZCS/man/man3 \
 LIB=OZCL/perl5
PERL5LIB=OZCL/perl5 make test

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
* Wed Sep 25 2019 Evgeniy Korneechev <ekorneechev@altlinux.org> VERSION-alt1.zimbra8.8.15
- Initial build for p8

