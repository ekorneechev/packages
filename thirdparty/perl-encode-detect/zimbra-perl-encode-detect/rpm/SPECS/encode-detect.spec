Summary:            Encode::Detect - An Encode::Encoding subclass that detects the encoding of data 
Name:               zimbra-perl-MODNORMNAME
Version:            VERSION
Release:            alt1
License:            MPL-1.1, GPL-2, LGPL-2.1
Source:             %{name}-%{version}.tar.gz
Packager:           Evgeniy Korneechev <ekorneechev@altlinux.org>
Group:              Development/Languages
BuildRequires:      zimbra-perl-base
Requires:           zimbra-perl-base
AutoReqProv:        no
URL:                https://metacpan.org/release/MODNAME

%description
This Perl module is an Encode::Encoding subclass that uses Encode::Detect::Detector
to determine the charset of the input data and then decodes it using the encoder of
the detected charset.

%define debug_package %{nil}

%prep
%setup -n MODNAME-%{version}

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
find %{buildroot} -name .packlist -exec rm -rf {} +
mkdir -p %{buildroot}OZCS/man/man3 %{buildroot}OZCL/perl5
find %{buildroot} -name *.3pm -exec cp {} %{buildroot}OZCS/man/man3 \;
find %{buildroot} -name %{perl_archname} -type d -exec cp -R {} %{buildroot}OZCL/perl5/ \;

%files
%defattr(-,root,root)
OZCL
OZCS/man

%changelog
* Wed Sep 25 2019 Evgeniy Korneechev <ekorneechev@altlinux.org> VERSION-alt1
- Initial build for p8

