Name:           font-tools
Version:        1.1.1
Release:        1%{?dist}
Summary:        A simple set of font manipolation utilities
License:        ASL 2.0
Group:          Applications/File
URL:            https://github.com/journeyman88/font-tools/
Source0:        https://github.com/journeyman88/font-tools/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildArch: 	noarch
BuildRoot:      %{_topdir}/BUILDROOT/
Requires:	fontforge woff2-tools ttf2eot libeot-tools

%description
font-tools is a set of scripts to convert fonts and create fully compatible webfonts.

%prep
%autosetup -n %{name}-%{version}

%build

%install
rm -rf %{buildroot}
mkdir -p  %{buildroot}
mkdir -p %{buildroot}%{_bindir}
install -m755 font2ttf %{buildroot}%{_bindir}/
install -m755 font2otf %{buildroot}%{_bindir}/
install -m755 font2svg %{buildroot}%{_bindir}/
install -m755 font2woff %{buildroot}%{_bindir}/
install -m755 mkwebfont %{buildroot}%{_bindir}/
# Docs
mkdir -p %{buildroot}%{_defaultdocdir}/font-tools
install -m644 LICENSE.txt %{buildroot}%{_defaultdocdir}/font-tools/LICENSE.txt

%clean
rm -rf %{buildroot}

%files
%attr(755, root, root) %{_bindir}/font2ttf
%attr(755, root, root) %{_bindir}/font2otf
%attr(755, root, root) %{_bindir}/font2svg
%attr(755, root, root) %{_bindir}/font2woff
%attr(755, root, root) %{_bindir}/mkwebfont
%attr(-, root, root) %{_defaultdocdir}/font-tools/

%changelog
* Fri Feb 12 2021 Marco Bignami <m.bignami@unknown-domain.no-ip.net> 1.1.1-1
 - Updated to upstream code.

* Tue Nov 20 2018 Marco Bignami <m.bignami@unknown-domain.no-ip.net> 1.1.0-1
 - Updated to upstream code.

* Wed Nov 14 2018 Marco Bignami <m.bignami@unknown-domain.no-ip.net> 1.0.3-2
 - Moved project to github.

* Mon Feb 26 2018 Marco Bignami <m.bignami@unknown-domain.no-ip.net> 1.0.3-1
 - New build.
 
* Wed Feb 08 2017 Marco Bignami <m.bignami@unknown-domain.no-ip.net> 1.0.2-1
 - Fixed bug in mkwebfont: error in conversion to ttf for woff, svg and otf
 
* Wed Feb 08 2017 Marco Bignami <m.bignami@unknown-domain.no-ip.net> 1.0.2-1
 - Fixed bug in mkwebfont: error in input file name for svg and otf
 
* Tue Feb 07 2017 Marco Bignami <m.bignami@unknown-domain.no-ip.net> 1.0.1-1
 - Fixed bug in mkwebfont

* Tue Feb 07 2017 Marco Bignami <m.bignami@unknown-domain.no-ip.net> 1.0.0-1
 - Created package
