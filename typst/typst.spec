#
# spec file for package typst

%global debug_package %{nil}

Name:           typst
Summary:        A new markup-based typesetting system that is powerful and easy to learn.
Version:        0.14.0
Release:        1%{?dist}
License:        Apache-2.0
Url:            https://github.com/typst/typst
Source0:        https://github.com/typst/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}
BuildRequires:  wget
BuildRequires:  gcc
BuildRequires:  openssl-devel

%description
Typst is a new markup-based typesetting system that is designed to be as powerful as LaTeX while being much easier to learn and use.

%prep
%autosetup -n %{name}-%{version}

%build
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs > rustup-install
sh rustup-install --profile default --default-toolchain stable -y
. "$HOME/.cargo/env"
cargo build --release

%install
mkdir -p %{buildroot}/%{_bindir}
install -m 755 target/release/typst %{buildroot}/%{_bindir}/typst

# Docs
mkdir -p %{buildroot}%{_defaultdocdir}/typst
install -m644 CONTRIBUTING.md %{buildroot}%{_defaultdocdir}/typst/CONTRIBUTING.md
install -m644 LICENSE %{buildroot}%{_defaultdocdir}/typst/LICENSE
install -m644 NOTICE %{buildroot}%{_defaultdocdir}/typst/NOTICE
install -m644 README.md %{buildroot}%{_defaultdocdir}/typst/README.md

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%attr(755, root, root) %{_bindir}/typst
%attr(-, root, root) %{_defaultdocdir}/typst

%changelog
* Mon Nov 03 2025 Marco Bignami <m.bignami@unknown-domain.no-ip.net> 0.14.0-1
 - Updated package to upstream

* Fri Mar 21 2025 Marco Bignami <m.bignami@unknown-domain.no-ip.net> 0.13.1-1
 - Updated package to upstream

* Tue Feb 25 2025 Marco Bignami <m.bignami@unknown-domain.no-ip.net> 0.13.0-2
 - Switching to rustup to manage rust allowing older distro builds.

* Tue Feb 25 2025 Marco Bignami <m.bignami@unknown-domain.no-ip.net> 0.13.0-1
 - Updated package to upstream

* Thu Jan 16 2025 Marco Bignami <m.bignami@unknown-domain.no-ip.net> 0.12.0-1
 - Initial package.
