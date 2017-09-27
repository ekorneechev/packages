Summary:            BerkeleyDB - Perl extension for Berkeley DB version 2, 3, 4 or 5
Name:               zimbra-perl-MODNORMNAME
Version:            VERSION
Release:            alt1.zimbra844
License:            GPL+ or Artistic
Source:             %{name}-%{version}.tar.gz
Packager:           Korneechev Evgeniy <ekorneechev@altlinux.org>
Group:              Development/Languages
BuildRequires:      zimbra-perl-base, zimbra-bdb-devel
Requires:           zimbra-perl-base, zimbra-bdb-libs
AutoReqProv:        no
URL:                https://metacpan.org/release/MODNAME

%description
This Perl module provides an interface to most of the functionality available
in Berkeley DB versions 2, 3, 5 and 6. In general it is safe to assume that
the interface provided here to be identical to the Berkeley DB interface. The
main changes have been to make the Berkeley DB API work in a Perl way. Note
that if you are using Berkeley DB 2.x, the new features available in Berkeley
DB 3.x or later are not available via this module.

%define debug_package %{nil}

%prep
%setup -n MODNAME-%{version}
%set_verify_elf_method skip

%build
export BERKELEYDB_LIB=OZCL; \
export BERKELEYDB_INCLUDE=OZCI; \
perl -I OZCL/perl5 Makefile.PL INSTALL_BASE=OZC \
 INSTALLSITEMAN1DIR=OZCS/man/man1 INSTALLSITEMAN3DIR=OZCS/man/man3 \
 INSTALLMAN3DIR=OZCS/man/man1 INSTALLVENDORMAN3DIR=OZCS/man/man1 \
 INSTALLMAN3DIR=OZCS/man/man3 INSTALLVENDORMAN3DIR=OZCS/man/man3 \
 LIB=OZCL/perl5
LD_RUN_PATH=OZCL PERL5LIB=OZCL/perl5 make test

# remove .packlist and perllocal.pod
#  $(DESTINSTALLSITEARCH)/auto/$(FULLEXT)/.packlist
#  $(DESTINSTALLSITEARCH)/perllocal.pod
%define perl_archname %(perl -MConfig -e 'print $Config{archname}')
%install
make install DESTDIR=${RPM_BUILD_ROOT}
rm -f %{buildroot}OZCL/perl5/%{perl_archname}/perllocal.pod
rm -f %{buildroot}OZCL/perl5/%{perl_archname}/auto/*/.packlist

%files
%defattr(-,root,root)
OZCL
OZCS/man
