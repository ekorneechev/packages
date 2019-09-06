Summary:            Config::IniFiles - A module for reading .ini-style configuration files
Name:               zimbra-perl-MODNORMNAME
Version:            VERSION
Release:            alt1.zimbra8.8.15
License:            GPL+ or Artistic
Source:             %{name}-%{version}.tar.gz
Packager:           Korneechev Evgeniy <ekorneechev@altlinux.org>
Group:              Development/Languages
BuildRequires:      zimbra-perl-base, zimbra-perl-list-moreutils
Requires:           zimbra-perl-base, zimbra-perl-list-moreutils
AutoReqProv:        no
URL:                https://metacpan.org/release/MODNAME

%description
Config::IniFiles provides a way to have readable configuration files
outside your Perl script. Configurations can be imported (inherited,
stacked,...), sections can be grouped, and settings can be accessed from
a tied hash.

%define debug_package %{nil}

%prep
%setup -n MODNAME-%{version}

%build
perl -I OZCL/perl5 Makefile.PL INSTALL_BASE=OZC \
 INSTALLSITEMAN1DIR=OZCS/man/man1 INSTALLSITEMAN3DIR=OZCS/man/man3 \
 INSTALLMAN3DIR=OZCS/man/man1 INSTALLVENDORMAN3DIR=OZCS/man/man1 \
 INSTALLMAN3DIR=OZCS/man/man3 INSTALLVENDORMAN3DIR=OZCS/man/man3 \
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
find %{buildroot} -name Config -type d -exec cp -R {} %{buildroot}OZCL/perl5 \;

%files
%defattr(-,root,root)
OZCL
OZCS/man
