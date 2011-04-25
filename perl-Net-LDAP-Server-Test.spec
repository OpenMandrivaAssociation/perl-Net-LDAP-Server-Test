%define upstream_name    Net-LDAP-Server-Test
%define upstream_version 0.10

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:    Test Net::LDAP code
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Net/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Data::Dump)
BuildRequires: perl(IO::Select)
BuildRequires: perl(IO::Socket)
BuildRequires: perl(Net::LDAP)
BuildRequires: perl(Net::LDAP::Server)
BuildRequires: perl(Test::More)

BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
Now you can test your Net::LDAP code without having a real LDAP server
available.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*
