#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Encode
Summary:	Encode - character encodings
Summary(pl.UTF-8):	Encode - kodowania znaków
Name:		perl-Encode
Version:	2.70
Release:	1
Epoch:		1
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Encode/DANKOGAI/%{pdir}-%{version}.tar.gz
# Source0-md5:	91af5a434c48ccdc8ceebc9dfd75fe1c
URL:		http://search.cpan.org/dist/Encode/
BuildRequires:	perl-devel >= 1:5.8.0
%{?with_tests:BuildRequires:	perl-parent >= 0.221}
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl-parent >= 0.221
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

install -d $RPM_BUILD_ROOT%{perl_vendorlib}/Encode

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS Changes README
%attr(755,root,root) %{_bindir}/enc2xs
%attr(755,root,root) %{_bindir}/encguess
%attr(755,root,root) %{_bindir}/piconv
%{perl_vendorarch}/Encode.pm
%{perl_vendorarch}/encoding.pm
# FIXME: *.h to devel(?), check out the use for *.e2x files
%{perl_vendorarch}/Encode
%dir %{perl_vendorarch}/auto/Encode
%dir %{perl_vendorarch}/auto/Encode/*/
%attr(755,root,root) %{perl_vendorarch}/auto/Encode/*/*.so
%dir %{perl_vendorlib}/Encode
%{_mandir}/man1/enc2xs.1*
%{_mandir}/man1/encguess.1*
%{_mandir}/man1/piconv.1*
%{_mandir}/man3/Encode*.3pm*
%{_mandir}/man3/encoding.3pm*
