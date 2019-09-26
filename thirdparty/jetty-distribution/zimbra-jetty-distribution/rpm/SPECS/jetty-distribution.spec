Summary:            Zimbra's jetty-distribution build
Name:               zimbra-jetty-distribution
Version:            VERSION
Release:            alt1
License:            Apache-2.0
Source:             %{name}-%{version}.tar.gz
Requires:           zimbra-store-base
AutoReqProv:        no
URL:                https://www.eclipse.org/jetty/
Group:              Development/Java

%define debug_package %{nil}

%description
The Zimbra jetty-distribution build

%changelog
* Wed Sep 25 2019 Evgeniy Korneechev <ekorneechev@altlinux.org> VERSION-alt1
- Initial build for p8


%prep
%setup -n jetty-distribution-%{version}

%build

%install
mkdir -p ${RPM_BUILD_ROOT}/opt/zimbra/common/jetty_home
find -maxdepth 1 -mindepth 1 | grep -v -w -e debian -e rpm | xargs -r '-I{}' cp -a '{}' ${RPM_BUILD_ROOT}/opt/zimbra/common/jetty_home

%files
%defattr(-,root,root)
/opt/zimbra/common/jetty_home
