Summary:            SSL sockets with IO::Socket interface
Name:               zimbra-perl-io-socket-ssl
Version:            VERSION
Release:            alt1
License:            GPL+ or Artistic
Source:             %{name}-%{version}.tar.gz
Packager:           Evgeniy Korneechev <ekorneechev@altlinux.org>
Group:              Development/Languages
BuildRequires:      zimbra-perl-base, zimbra-perl-mozilla-ca, zimbra-perl-net-ssleay
BuildRequires:      zimbra-perl-io-socket-ip
Requires:           zimbra-perl-base, zimbra-perl-mozilla-ca, zimbra-perl-net-ssleay
Requires:           zimbra-perl-io-socket-ip
AutoReqProv:        no
URL:                https://metacpan.org/release/IO-Socket-SSL

%description
IO::Socket::SSL makes using SSL/TLS much easier by wrapping the
necessary functionality into the familiar IO::Socket interface and
providing secure defaults whenever possible. This way, existing
applications can be made SSL-aware without much effort, at least if
you do blocking I/O and don't use select or poll.

%define debug_package %{nil}

%prep
%setup -n IO-Socket-SSL-%{version}

%build
export NO_NETWORK_TESTING="TRUE"; \
perl -I OZCL/perl5 Makefile.PL INSTALL_BASE=OZC \
 INSTALLSITEMAN1DIR=OZCS/man/man1 INSTALLSITEMAN3DIR=OZCS/man/man3 \
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
* Wed Sep 25 2019 Evgeniy Korneechev <ekorneechev@altlinux.org> VERSION-alt1
- Initial build for p8

