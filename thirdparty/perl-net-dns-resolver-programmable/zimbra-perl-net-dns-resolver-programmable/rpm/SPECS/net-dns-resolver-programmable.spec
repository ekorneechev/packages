Summary:            Net::DNS::Resolver::Programmable - programmable DNS resolver class for offline emulation of DNS
Name:               zimbra-perl-MODNORMNAME
Version:            VERSION
Release:            alt1
License:            GPL-2 or Artistic
Source:             %{name}-%{version}.tar.gz
Packager:           Evgeniy Korneechev <ekorneechev@altlinux.org>
Group:              Development/Languages
BuildRequires:      zimbra-perl-base, zimbra-perl-net-dns
Requires:           zimbra-perl-base, zimbra-perl-net-dns
AutoReqProv:        no
URL:                https://metacpan.org/release/MODNAME

%description
Net::DNS::Resolver::Programmable is a Net::DNS::Resolver descendant class that
allows a virtual DNS to be emulated instead of querying the real DNS.  A set
of static DNS records may be supplied, or arbitrary code may be specified as a
means for retrieving DNS records, or even generating them on the fly.

%define debug_package %{nil}

%prep
%setup -n MODNAME-v%{version}

%build
perl -I OZCL/perl5 Makefile.PL INSTALL_BASE=OZC \
 INSTALLSITEMAN1DIR=OZCS/man/man1 INSTALLSITEMAN3DIR=OZCS/man/man3 \
 INSTALLMAN3DIR=OZCS/man/man1 INSTALLVENDORMAN3DIR=OZCS/man/man1 \
 INSTALLMAN3DIR=OZCS/man/man3 INSTALLVENDORMAN3DIR=OZCS/man/man3
 LIB=OZCL/perl5
PERL5LIB=OZCL/perl5 make test

# remove .packlist and perllocal.pod
#  $(DESTINSTALLSITEARCH)/auto/$(FULLEXT)/.packlist
#  $(DESTINSTALLSITEARCH)/perllocal.pod
%define perl_archname %(perl -MConfig -e 'print $Config{archname}')
%install
make install DESTDIR=${RPM_BUILD_ROOT}
find %{buildroot} -name %{perl_archname} -type d -exec rm -rf {} +
mkdir -p %{buildroot}OZCS/man/man3 %{buildroot}OZCL/perl5
find %{buildroot} -name *.3pm -exec cp {} %{buildroot}OZCS/man/man3 \;
find %{buildroot} -name Net -type d -exec cp -R {} %{buildroot}OZCL/perl5 \;

%files
%defattr(-,root,root)
OZCL
OZCS/man

%changelog
* Wed Sep 25 2019 Evgeniy Korneechev <ekorneechev@altlinux.org> VERSION-alt1
- Initial build for p8

