#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Class-Accessor
Version  : 0.51
Release  : 20
URL      : https://cpan.metacpan.org/authors/id/K/KA/KASEI/Class-Accessor-0.51.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/K/KA/KASEI/Class-Accessor-0.51.tar.gz
Summary  : unknown
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-Class-Accessor-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
NAMES
Class::Accessor         - automated accessor generation
Class::Accessor::Fast   - faster automated accessor generation
Class::Accessor::Faster - even faster, using an array

%package dev
Summary: dev components for the perl-Class-Accessor package.
Group: Development
Provides: perl-Class-Accessor-devel = %{version}-%{release}
Requires: perl-Class-Accessor = %{version}-%{release}

%description dev
dev components for the perl-Class-Accessor package.


%package perl
Summary: perl components for the perl-Class-Accessor package.
Group: Default
Requires: perl-Class-Accessor = %{version}-%{release}

%description perl
perl components for the perl-Class-Accessor package.


%prep
%setup -q -n Class-Accessor-0.51
cd %{_builddir}/Class-Accessor-0.51

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Class::Accessor.3
/usr/share/man/man3/Class::Accessor::Fast.3
/usr/share/man/man3/Class::Accessor::Faster.3

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.34.0/Class/Accessor.pm
/usr/lib/perl5/vendor_perl/5.34.0/Class/Accessor/Fast.pm
/usr/lib/perl5/vendor_perl/5.34.0/Class/Accessor/Faster.pm
