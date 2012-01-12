#
# Conditional build:
%bcond_without	autodeps	# don't BR packages needed only for resolving deps
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Net
%define		pnam	IDN-Nameprep
Summary:	IDN nameprep tools
Summary(pl.UTF-8):	Narzędzia obsługujące specyfikację IDN nameprep
Name:		perl-Net-IDN-Nameprep
Version:	1.101
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Net/CFAERBER/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	716a9400c55bde1c20136b0bef585557
URL:		http://search.cpan.org/dist/IDN-Nameprep/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with autodeps} || %{with tests}
BuildRequires:	perl-Unicode-Stringprep >= 1.1
%endif
%if %{with tests}
BuildRequires:	perl-Test-Simple
BuildRequires:	perl-Test-NoWarnings
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
%doc Changes README
%{perl_vendorlib}/Net/IDN/Nameprep.pm
%{_mandir}/man3/Net::IDN::Nameprep.3pm*
