#
# Conditional build:
%bcond_without	tests	# unit tests
#
%define	pdir	Encode
Summary:	Encode - character encodings
Summary(pl.UTF-8):	Encode - kodowania znaków
Name:		perl-Encode
Version:	3.17
Release:	1
Epoch:		2
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Encode/%{pdir}-%{version}.tar.gz
# Source0-md5:	c55a11554641517ae7b04bf2ec53b271
URL:		https://metacpan.org/release/Encode
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	rpmbuild(macros) >= 1.745
%if %{with tests}
BuildRequires:	perl(Exporter) >= 5.57
BuildRequires:	perl-Test-Simple >= 0.81_01
BuildRequires:	perl-parent >= 0.221
%endif
Requires:	perl-parent >= 0.221
Obsoletes:	perl-Encode-compat < 0.08
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

# rename to avoid conflict with perl-tools
mv $RPM_BUILD_ROOT%{_bindir}/encguess{,-tool}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS Changes README
%attr(755,root,root) %{_bindir}/enc2xs
%attr(755,root,root) %{_bindir}/encguess-tool
%attr(755,root,root) %{_bindir}/piconv
%{perl_vendorarch}/Encode.pm
%{perl_vendorarch}/encoding.pm
# FIXME: *.h to devel(?), check out the use for *.e2x files
%{perl_vendorarch}/Encode
%dir %{perl_vendorarch}/auto/Encode
%attr(755,root,root) %{perl_vendorarch}/auto/Encode/Encode.so
%dir %{perl_vendorarch}/auto/Encode/Byte
%attr(755,root,root) %{perl_vendorarch}/auto/Encode/Byte/Byte.so
%dir %{perl_vendorarch}/auto/Encode/CN
%attr(755,root,root) %{perl_vendorarch}/auto/Encode/CN/CN.so
%dir %{perl_vendorarch}/auto/Encode/EBCDIC
%attr(755,root,root) %{perl_vendorarch}/auto/Encode/EBCDIC/EBCDIC.so
%dir %{perl_vendorarch}/auto/Encode/JP
%attr(755,root,root) %{perl_vendorarch}/auto/Encode/JP/JP.so
%dir %{perl_vendorarch}/auto/Encode/KR
%attr(755,root,root) %{perl_vendorarch}/auto/Encode/KR/KR.so
%dir %{perl_vendorarch}/auto/Encode/Symbol
%attr(755,root,root) %{perl_vendorarch}/auto/Encode/Symbol/Symbol.so
%dir %{perl_vendorarch}/auto/Encode/TW
%attr(755,root,root) %{perl_vendorarch}/auto/Encode/TW/TW.so
%dir %{perl_vendorarch}/auto/Encode/Unicode
%attr(755,root,root) %{perl_vendorarch}/auto/Encode/Unicode/Unicode.so
%dir %{perl_vendorlib}/Encode
%{_mandir}/man1/enc2xs.1*
%{_mandir}/man1/encguess.1*
%{_mandir}/man1/piconv.1*
%{_mandir}/man3/Encode*.3pm*
%{_mandir}/man3/encoding.3pm*
