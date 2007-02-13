#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Net
%define		pnam	IDN-Nameprep
Summary:	IDN nameprep tools
Summary(pl.UTF-8):	Narzędzia obsługujące specyfikację IDN nameprep
Name:		perl-Net-IDN-Nameprep
Version:	0.02
Release:	4
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	092b55a6973d702f163ed2e921fc30e1
URL:		http://search.cpan.org/dist/IDN-Nameprep/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with autodeps} || %{with tests}
BuildRequires:	perl-Unicode-String
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreq	'perl(v5.6.0)'

%description
Net::IDN::Nameprep implements IDN nameprep specification. This module
exports only one function called nameprep.

%description -l pl.UTF-8
Net::IDN::Nameprep jest implementacją specyfikacji IDN nameprep. Ten
moduł eksportuje tylko jedną funkcję o nazwie nameprep.

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
%doc Changes
%{perl_vendorlib}/Net/IDN/Nameprep.pm
%{perl_vendorlib}/Net/IDN/Nameprep
%{_mandir}/man3/*
