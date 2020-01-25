#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	HTTP
%define		pnam	Request-Form
Summary:	HTTP::Request::Form - construct HTTP::Request objects for form processing
Summary(pl.UTF-8):	HTTP::Request::Form - tworzenie obiektów HTTP::Request do przetwarzania formularzy
Name:		perl-HTTP-Request-Form
Version:	0.952
Release:	6
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	2d8e8af81725b1e5090f5e921f45c6cd
URL:		http://search.cpan.org/dist/HTTP-Request-Form/
BuildRequires:	perl-HTML-Tree
BuildRequires:	perl-URI
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	perl-libwww
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is an extension of the HTTP::Request suite. It allows easy
processing of forms in a user agent by filling out fields, querying
fields, selections and buttons and pressing buttons. It uses
HTML::TreeBuilder generated parse trees of documents (especially the
forms parts extracted with extract_links) and generates it's own
internal representation of forms from which it then generates the
request objects to process the form application.

%description -l pl.UTF-8
Ten moduł jest rozszerzeniem zestawu HTTP::Request. Pozwala na łatwe
przetwarzanie formularzy po stronie klienta poprzez wypełnianie pól,
odczyt zawartości pól, zaznaczanie oraz naciskanie przycisków. Używa
wygenerowanych przez HTML::TreeBuilder drzew analizy dokumentów
(szczególnie do części formularzy wyciągniętych przez extract_links) i
generuje własną wewnętrzną reprezentację formularzy, z których
następnie generuje obiekty żądań do przetworzenia całości.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/HTTP/Request/Form.pm
%{_mandir}/man3/*
