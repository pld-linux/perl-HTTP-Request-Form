%include	/usr/lib/rpm/macros.perl
%define	pdir	HTTP
%define	pnam	Request-Form
Summary:	HTTP::Request::Form - Construct HTTP::Request objects for form processing
Summary(pl):	HTTP::Request::Form - tworzenie obiektów HTTP::Request do przetwarzania formularzy
Name:		perl-HTTP-Request-Form
Version:	0.952
Release:	4
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	perl-HTML-Tree
BuildRequires:	perl-URI
BuildRequires:	perl-libwww
BuildRequires:	rpm-perlprov >= 4.0.2-104
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

%description -l pl
Ten modu³ jest rozszerzeniem zestawu HTTP::Request. Pozwala na ³atwe
przetwarzanie formularzy po stronie klienta poprzez wype³nianie pól,
odczyt zawarto¶ci pól, zaznaczanie oraz naciskanie przycisków. U¿ywa
wygenerowanych przez HTML::TreeBuilder drzew analizy dokumentów
(szczególnie do czê¶ci formularzy wyci±gniêtych przez extract_links) i
generuje w³asn± wewnêtrzn± reprezentacjê formularzy, z których
nastêpnie generuje obiekty ¿±dañ do przetworzenia ca³o¶ci.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_sitelib}/HTTP/Request/Form.pm
%{_mandir}/man3/*
