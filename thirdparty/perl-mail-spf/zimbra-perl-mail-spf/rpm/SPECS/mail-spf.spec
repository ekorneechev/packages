Summary:            Mail::SPF - An object-oriented implementation of Sender Policy Framework
Name:               zimbra-perl-MODNORMNAME
Version:            VERSION
Release:            alt1.zimbra8.8.15
License:            MIT
Source:             %{name}-%{version}.tar.gz
Packager:           Korneechev Evgeniy <ekorneechev@altlinux.org>
Group:              Development/Languages
BuildRequires:      zimbra-perl-base, zimbra-perl-error, zimbra-perl-netaddr-ip
BuildRequires:      zimbra-perl-net-dns, zimbra-perl-net-dns-resolver-programmable
Requires:           zimbra-perl-base, zimbra-perl-error, zimbra-perl-netaddr-ip
Requires:           zimbra-perl-net-dns, zimbra-perl-net-dns-resolver-programmable
AutoReqProv:        no
URL:                https://metacpan.org/release/MODNAME

%description
Mail::SPF is an object-oriented implementation of Sender Policy Framework (SPF).
See http://www.openspf.org for more information about SPF.
This class collection aims to fully conform to the SPF specification (RFC 4408)
so as to serve both as a production quality SPF implementation and as a reference
for other developers of SPF implementations.

%define debug_package %{nil}

%prep
%setup -n MODNAME-v%{version}

%build
perl -I OZCL/perl5 Makefile.PL INSTALL_BASE=OZC \
 INSTALLSITEMAN1DIR=OZCS/man/man1 INSTALLSITEMAN3DIR=OZCS/man/man3 \
 INSTALLMAN3DIR=OZCS/man/man1 INSTALLVENDORMAN3DIR=OZCS/man/man1 \
 INSTALLMAN3DIR=OZCS/man/man3 INSTALLVENDORMAN3DIR=OZCS/man/man3 \
 LIB=OZCL/perl5
PERL5LIB=OZCL/perl5 make

# remove .packlist and perllocal.pod
#  $(DESTINSTALLSITEARCH)/auto/$(FULLEXT)/.packlist
#  $(DESTINSTALLSITEARCH)/perllocal.pod
%define perl_archname %(perl -MConfig -e 'print $Config{archname}')
%install
make install DESTDIR=${RPM_BUILD_ROOT}
mkdir -p %{buildroot}OZCS/man/man3 %{buildroot}OZCL/perl5
find %{buildroot} -name %{perl_archname} -type d -exec rm -rf {} +
find %{buildroot} -name *.3pm -exec cp {} %{buildroot}OZCS/man/man3 \;
find %{buildroot} -name Mail -type d -exec cp -R {} %{buildroot}OZCL/perl5 \;

%files
%defattr(-,root,root)
OZCL
OZCS/man

%changelog
* Wed Sep 25 2019 Evgeniy Korneechev <ekorneechev@altlinux.org> VERSION-alt1.zimbra8.8.15
- Initial build for p8

