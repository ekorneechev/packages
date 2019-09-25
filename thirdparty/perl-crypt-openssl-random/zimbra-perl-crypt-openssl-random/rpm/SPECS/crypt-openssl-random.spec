Summary:            Zimbra's Crypt::OpenSSL::Random build
Name:               zimbra-perl-crypt-openssl-random
Version:            VERSION
Release:            alt1.zimbra8.8.15
License:            GPL-2
Source:             %{name}-%{version}.tar.gz
BuildRequires:      zimbra-perl-base, zimbra-openssl-devel
Requires:           zimbra-perl-base, zimbra-openssl-libs
AutoReqProv:        no
URL:                http://search.cpan.org/dist/Crypt-OpenSSL-Random/
Group:              Development/Perl

%define perl_archname %(eval "`perl -V:archname`"; echo $archname)

%description
The Zimbra Crypt::OpenSSL::Random build

%define debug_package %{nil}

%prep
%setup -n Crypt-OpenSSL-Random-%{version}
%set_verify_elf_method skip

%build
LDFLAGS="-Wl,-rpath,OZCL"; export LDFLAGS; \
CFLAGS="-O2 -g"; export CFLAGS; \
perl -I OZCL/perl5 Makefile.PL INSTALL_BASE=OZC \
 INSTALLSITEMAN1DIR=OZCS/man/man1 INSTALLSITEMAN3DIR=OZCS/man/man3 \
 LIB=OZCL/perl5 LIBS="-LOZCL -lssl -lcrypto" INC="-IOZCI"
LD_RUN_PATH=OZCL make

%install
LD_RUN_PATH=OZCL make install DESTDIR=${RPM_BUILD_ROOT}
rm -f %{buildroot}OZCL/perl5/%{perl_archname}/perllocal.pod
rm -f %{buildroot}OZCL/perl5/%{perl_archname}/auto/*/*/*/.packlist

%files
%defattr(-,root,root)
OZCL
OZCS/man

%changelog
* Wed Sep 25 2019 Evgeniy Korneechev <ekorneechev@altlinux.org> VERSION-alt1.zimbra8.8.15
- Initial build for p8

