Name:           ttf2eot
Version:        0.0.3
Release:        2%{?dist}
Summary:        This package contains tools to convert TTF into EOT
License:        LGPLv2
Group:          Applications/File
URL:            https://github.com/wget/ttf2eot
Source0:        https://github.com/wget/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRoot:      %{_topdir}/BUILDROOT/
BuildRequires:  make,gcc,glibc-devel,gcc-c++

%description
This is a tool to convert TrueType/OpenType Fonts to Embeddable Open Type
the font format used by Internet Explorer for font-face declatrations.

%prep
%autosetup -n %{name}-%{version}

%build
CFLAGS="${CFLAGS:-%optflags}" ; export CFLAGS
CXXFLAGS="${CXXFLAGS:-%optflags}" ; export CXXFLAGS
FFLAGS="${FFLAGS:-%optflags}" ; export FFLAGS
%__make %{?_smp_mflags}

%install
rm -rf %{buildroot}
mkdir -p  %{buildroot}
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_defaultdocdir}/%{name}/
install -m755 ttf2eot %{buildroot}%{_bindir}/
install -m644 ChangeLog %{buildroot}%{_defaultdocdir}/%{name}/
install -m644 README %{buildroot}%{_defaultdocdir}/%{name}/

%clean
rm -rf %{buildroot}

%files
%attr(755, root, root) %{_bindir}/ttf2eot
%attr(-, root, root) %{_defaultdocdir}/%{name}/README
%attr(-, root, root) %{_defaultdocdir}/%{name}/ChangeLog

%changelog
* Wed Nov 14 2018 Marco Bignami <m.bignami@unknown-domain.no-ip.net> 0.0.3-2
 - Cleaned up the spec file.
* Fri Feb 3 2017 Marco Bignami <m.bignami@unknown-domain.no-ip.net> 0.0.3-1
 - First build of package
