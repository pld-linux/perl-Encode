#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Encode
Summary:	Encode - character encodings
Summary(pl.UTF-8):	Encode - kodowania znaków
Name:		perl-Encode
Version:	2.23
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Encode/%{pdir}-%{version}.tar.gz
# Source0-md5:	0b96a73d0bf7586946b651a0e30cfe17
URL:		http://search.cpan.org/dist/Encode/
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
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# man pages overlap with perl-modules
rm -rf $RPM_BUILD_ROOT%{_mandir}/man[13]

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS Changes README
%attr(755,root,root) %{_bindir}/*
%{perl_vendorarch}/Encode.pm
%{perl_vendorarch}/encoding.pm
%{perl_vendorarch}/Encode
%dir %{perl_vendorarch}/auto/Encode
%attr(755,root,root) %{perl_vendorarch}/auto/Encode/Encode.so
%{perl_vendorarch}/auto/Encode/Encode.bs
%dir %{perl_vendorarch}/auto/Encode/Byte
%dir %{perl_vendorarch}/auto/Encode/CN
%dir %{perl_vendorarch}/auto/Encode/EBCDIC
%dir %{perl_vendorarch}/auto/Encode/JP
%dir %{perl_vendorarch}/auto/Encode/KR
%dir %{perl_vendorarch}/auto/Encode/Symbol
%dir %{perl_vendorarch}/auto/Encode/TW
%dir %{perl_vendorarch}/auto/Encode/Unicode
%attr(755,root,root) %{perl_vendorarch}/auto/Encode/*/*.so
%{perl_vendorarch}/auto/Encode/*/*.bs
