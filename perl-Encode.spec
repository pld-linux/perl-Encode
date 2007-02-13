#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Encode
Summary:	Encode - character encodings
Summary(pl.UTF-8):	Encode - kodowania znaków
Name:		perl-Encode
Version:	2.18
Release:	0.1
License:	unknown (same as perl?)
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{version}.tar.gz
# Source0-md5:	b16ee372b5289303c1863c0371e4d3d9
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Encode module provides the interfaces between Perl's strings and
the rest of the system.

%description -l pl.UTF-8
Moduł Encode udostępnia interfejs pomiędzy łańcuchami w wewnętrznym
formacie Perla a resztą systemu.

%prep
%setup -q -n %{pdir}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS Changes README
%attr(755,root,root) %{_bindir}/*
%{perl_vendorarch}/*.pm
%{perl_vendorarch}/Encode
%dir %{perl_vendorarch}/auto/Encode
%dir %{perl_vendorarch}/auto/Encode/*/
%attr(755,root,root) %{perl_vendorarch}/auto/Encode/*.so
%attr(755,root,root) %{perl_vendorarch}/auto/Encode/*/*.so
%attr(755,root,root) %{perl_vendorarch}/auto/Encode/*/*.bs
#%{_mandir}/man?/*
