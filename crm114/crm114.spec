Summary:	Controllable Regex Mutilator: multi-method content classifier and filter
Name:		crm114
Version:	1.0.0
Release:	1
URL:		http://crm114.sourceforge.net/
License:	GPLv3
Group:		Applications/Text
Source0:	https://github.com/journeyman88/crm114/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRoot:      %{_topdir}/BUILDROOT/
BuildRequires:  cmake,make,gcc,glibc-devel,tre-devel

%if 0%{?rhel}
BuildRequires:	cmake3
%define bldcmd	cmake3
%endif
%if 0%{?fedora}
BuildRequires:	cmake
%define bldcmd	cmake
%endif

%description
CRM114 is a system to examine incoming e-mail, system log streams,
data files or other data streams, and to sort, filter, or alter the
incoming files or data streams according to the user's wildest
desires. Criteria for categorization of data can be by satisfaction of
regexps, by sparse binary polynomial matching with a Bayesian Chain
Rule evaluator, or by other means.

%package emacs
Summary: CRM114 mode for Emacs
Group: Applications/Text
Requires: emacs-el

%description emacs
Major Emacs mode for editing crm114 scripts.

%prep
%setup -q -n %{name}-%{version}

%build
mkdir build
cd build
CFLAGS="${CFLAGS:-%optflags}" ; export CFLAGS
CXXFLAGS="${CXXFLAGS:-%optflags}" ; export CXXFLAGS
FFLAGS="${FFLAGS:-%optflags}" ; export FFLAGS
%bldcmd -DCMAKE_INSTALL_PREFIX="/usr" -DCMAKE_INSTALL_LIBDIR=%{_libdir} \
      -DCMAKE_INSTALL_BINDIR=%{_bindir} -DCMAKE_INSTALL_SBINDIR=%{_sbindir} \
      -DCMAKE_INSTALL_SYSCONFDIR=%{_sysconfdir} -DCMAKE_INSTALL_MANDIR=%{_mandir} \
      -DCMAKE_INSTALL_DATAROOTDIR=%{_datarootdir} \
      ..
%__make %{?_smp_mflags}

%clean
rm -rf %{buildroot}

%install
rm -rf %{buildroot}
mkdir -p  %{buildroot}
cd build
%__make install DESTDIR=%{buildroot}

#%check
#make megatest

%files
%defattr(-,root,root,-)
%{_bindir}/*
%{_sysconfdir}/%{name}
%{_libdir}/%{name}
%{_datadir}/doc/%{name}
%{_mandir}/man1/*


%files emacs
%defattr(644,root,root,755)
%{_datadir}/emacs/site-lisp/*.el

%changelog
* Fri Nov 24 2023 Marco Bignami <m.bignami@unknown-domain.no-ip.net> 1.0.0-1
 - Rework for migration to git managed repo
 
* Thu Jun 30 2016 Marco Bignami <m.bignami@unknown-domain.no-ip.net> 0-1.20100106
 - Created spec for crm114 based upon the package in EPEL6
