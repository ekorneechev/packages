Summary:            IO::HTML - Open an HTML file with automatic charset detection 
Name:               zimbra-perl-io-html
Version:            VERSION
Release:            alt1.zimbra8.8.15
License:            GPL+ or Artistic
Source:             %{name}-%{version}.tar.gz
Packager:           Korneechev Evgeniy <ekorneechev@altlinux.org>
Group:              Development/Languages
BuildRequires:      zimbra-perl-base
Requires:           zimbra-perl-base
AutoReqProv:        no
URL:                https://metacpan.org/release/IO-HTML

%description
This module opens a file and performs automatic charset detection
based on the HTML5 algorithm.  You can then pass the filehandle to
HTML::Parser or a related module (or just read it yourself)

%define debug_package %{nil}

%prep
%setup -n IO-HTML-%{version}

%build
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
* Wed Sep 25 2019 Evgeniy Korneechev <ekorneechev@altlinux.org> VERSION-alt1.zimbra8.8.15
- Initial build for p8

