%define gitcommit decb6815d3f0145471f5b14d50919061ff86767e

Summary:	Controllable Regex Mutilator: multi-method content classifier and filter
Name:		crm114
Version:	1.0.0
Release:	1
URL:		http://crm114.sourceforge.net/
License:	GPLv3
Group:		Applications/Text
Source0:	https://github.com/journeyman88/crm114/archive/%{gitcommit}.tar.gz#/%{name}-%{version}.tar.gz
BuildRoot:      %{_topdir}/BUILDROOT/
BuildRequires:  cmake,make,gcc,glibc-devel,tre-devel

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
%setup -q -n %{name}-%{gitcommit}

%build
mkdir build
cd build
cmake ..
%__make %{?_smp_mflags}

%clean
rm -rf %{buildroot}

%install
rm -rf %{buildroot}
mkdir -p  %{buildroot}
cd build
install -d %{buildroot}{%{_bindir},%{_mandir}/man1,%{_datadir}/{%{name},emacs/site-lisp}}
%__make install DESTDIR=%{buildroot}
install -pm 755 mail{filter,reaver,trainer,lib}.crm shuffle.crm %{buildroot}%{_datadir}/%{name}/
gzip -9 crm.1
gzip -9 cssdiff.1
gzip -9 cssutil.1
install -m 644 crm.1.gz cssdiff.1.gz cssutil.1.gz %{buildroot}%{_mandir}/man1/

#%check
#make megatest

%files
%defattr(-,root,root,-)
%doc README *.txt *.recipe *.example mailfilter.cf
%{_bindir}/*
%{_datadir}/%{name}
%{_mandir}/man1/*

%files emacs
%defattr(644,root,root,755)
%{_datadir}/emacs/site-lisp/*.el

%changelog
* Thu Nov 23 2023 Marco Bignami <m.bignami@unknown-domain.no-ip.net> 20100106-1
 - Rework for migration to git managed repo
 
* Thu Jun 30 2016 Marco Bignami <m.bignami@unknown-domain.no-ip.net> 0-1.20100106
 - Created spec for crm114 based upon the package in EPEL6
