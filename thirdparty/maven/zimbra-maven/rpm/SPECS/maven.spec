Summary:            Zimbra's maven build
Name:               zimbra-maven
Version:            VERSION
Release:            alt1
License:            Apache-2.0
Source:             %{name}-%{version}.tar.gz
Patch0:             skip_rat_build_xml.patch
BuildRequires:      zimbra-openjdk
Requires:           zimbra-openjdk
AutoReqProv:        no
URL:                https://maven.apache.org/
Group:              Development/Java

%description
The Zimbra maven build

%prep
%setup -n apache-maven-%{version}
%patch0 -p1

%build
ant

%install
mkdir -p $RPM_BUILD_ROOT/opt/zimbra/common/bin
cp -f build/bin/* $RPM_BUILD_ROOT/opt/zimbra/common/bin

%files
%defattr(-,root,root)
/opt/zimbra/common/bin


%changelog
* Wed Sep 25 2019 Evgeniy Korneechev <ekorneechev@altlinux.org> VERSION-alt1
- Initial build for p8

