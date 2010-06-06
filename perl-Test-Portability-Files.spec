#
# Conditional build:
%bcond_without	tests		# do not perform "make test"

%include	/usr/lib/rpm/macros.perl
%define		pdir	Test
%define		pnam	Portability-Files
Summary:	Test::Portability::Files - Check file names portability
Name:		perl-Test-Portability-Files
Version:	0.05
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Test/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	2ede77af4d3b82ffb39cd28fda6857e5
URL:		http://search.cpan.org/dist/Test-Portability-Files/
BuildRequires:	perl-Module-Build
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Test-Pod >= 1.00
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module is used to check the portability across operating systems
of the names of the files present in the distribution of a module. The
tests use the advices given in perlport/"Files and Filesystems". The
author of a distribution can select which tests to execute.

To use this module, simply copy the code from the synopsis in a test
file named t/portfs.t for example, and add it to your MANIFEST. You
can delete the call to options() to enable only most common tests.

By default, not all tests are enabled because some are judged too
cumbersome to be practical, especially since some of the most limited
platforms (like MS-DOS) seem to be no longer supported.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	destdir=$RPM_BUILD_ROOT \
	installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT
./Build install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%dir %{perl_vendorlib}/Test/Portability
%{perl_vendorlib}/Test/Portability/*.pm
%{_mandir}/man3/*
