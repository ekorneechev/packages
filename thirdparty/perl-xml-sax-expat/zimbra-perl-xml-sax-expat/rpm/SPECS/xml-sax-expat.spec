Summary:            XML::SAX::Expat - SAX2 Driver for Expat (XML::Parser)
Name:               zimbra-perl-MODNORMNAME
Version:            VERSION
Release:            alt1
License:            GPL+ or Artistic
Source:             %{name}-%{version}.tar.gz
Packager:           Evgeniy Korneechev <ekorneechev@altlinux.org>
Group:              Development/Languages
BuildRequires:      zimbra-perl-base, zimbra-perl-xml-sax, zimbra-perl-xml-parser
Requires:           zimbra-perl-base, zimbra-perl-xml-sax, zimbra-perl-xml-parser
AutoReqProv:        no
URL:                https://metacpan.org/release/MODNAME

%description
This is an implementation of a SAX2 driver sitting on top of
Expat (XML::Parser)

%define debug_package %{nil}

%prep
%setup -n MODNAME-%{version}

%build
export SKIP_SAX_INSTALL=1
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
PERL5LIB=OZCL/perl5:%{buildroot}OZCL/perl5 make install DESTDIR=${RPM_BUILD_ROOT}
rm -rf %{buildroot}OZCL/perl5/%{perl_archname}

%files
%defattr(-,root,root)
OZCL
OZCS/man

%post
/usr/bin/perl -I/opt/zimbra/common/lib/perl5 -MXML::SAX -e "XML::SAX->add_parser(q(XML::SAX::Expat))->save_parsers()"

%changelog
* Wed Sep 25 2019 Evgeniy Korneechev <ekorneechev@altlinux.org> VERSION-alt1
- Initial build for p8

