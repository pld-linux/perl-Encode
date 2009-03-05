#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Encode
Summary:	Encode - character encodings
Summary(pl.UTF-8):	Encode - kodowania znaków
Name:		perl-Encode
Version:	2.31
Release:	1
# same as in perl.spec package
Epoch:		1
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Encode/%{pdir}-%{version}.tar.gz
# Source0-md5:	ffaf2b5d6d703eefd4c501acf88597f8
URL:		http://search.cpan.org/dist/Encode/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Obsoletes:	perl-Encode-compat
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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS Changes README
%attr(755,root,root) %{_bindir}/*
%{perl_vendorarch}/Encode.pm
%{perl_vendorarch}/encoding.pm
# FIXME: *.h to devel(?), check out the use for *.e2x files
%{perl_vendorarch}/Encode
%dir %{perl_vendorarch}/auto/Encode
%dir %{perl_vendorarch}/auto/Encode/*/
%{perl_vendorarch}/auto/Encode/*/*.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Encode/*/*.so
%{_mandir}/man1/enc2xs.*
%{_mandir}/man1/piconv.*
%{_mandir}/man3/Encode*
%{_mandir}/man3/encoding.*
