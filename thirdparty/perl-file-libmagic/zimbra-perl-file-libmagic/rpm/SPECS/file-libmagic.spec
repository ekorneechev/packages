Summary:            File::LibMagic - Determine MIME types of data or files using libmagic
Name:               zimbra-perl-MODNORMNAME
Version:            VERSION
Release:            alt1
License:            GPL+ or Artistic
Source:             %{name}-%{version}.tar.gz
Packager:           Evgeniy Korneechev <ekorneechev@altlinux.org>
Group:              Development/Languages
BuildRequires:      zimbra-perl-base, libmagic-devel 
Requires:           zimbra-perl-base, libmagic
AutoReqProv:        no
URL:                https://metacpan.org/release/MODNAME

%description
This module allows Perl programmers to access and manipulate an LDAP
based Directory.

%define debug_package %{nil}

%prep
%setup -n MODNAME-%{version}

%build
perl -I OZCL/perl5 Makefile.PL INSTALL_BASE=OZC \
 INSTALLSITEMAN1DIR=OZCS/man/man1 INSTALLSITEMAN3DIR=OZCS/man/man3 \
 INSTALLMAN3DIR=OZCS/man/man1 INSTALLVENDORMAN3DIR=OZCS/man/man1 \
 INSTALLMAN3DIR=OZCS/man/man3 INSTALLVENDORMAN3DIR=OZCS/man/man3 \
 LIB=OZCL/perl5

# remove .packlist and perllocal.pod
#  $(DESTINSTALLSITEARCH)/auto/$(FULLEXT)/.packlist
#  $(DESTINSTALLSITEARCH)/perllocal.pod
%define perl_archname %(perl -MConfig -e 'print $Config{archname}')
%install
make install DESTDIR=${RPM_BUILD_ROOT}
rm -f %{buildroot}OZCL/perl5/%{perl_archname}/perllocal.pod
rm -f %{buildroot}OZCL/perl5/%{perl_archname}/auto/*/*/.packlist

%files
%defattr(-,root,root)
OZCL
OZCS/man

%changelog
* Wed Sep 25 2019 Evgeniy Korneechev <ekorneechev@altlinux.org> VERSION-alt1
- Initial build for p8

