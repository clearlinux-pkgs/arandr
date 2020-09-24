#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : arandr
Version  : 0.1.10
Release  : 5
URL      : https://gitlab.com/arandr/arandr/-/archive/0.1.10/arandr-0.1.10.tar.bz2
Source0  : https://gitlab.com/arandr/arandr/-/archive/0.1.10/arandr-0.1.10.tar.bz2
Summary  : Provide a simple visual front end for XRandR 1.2.
Group    : Development/Tools
License  : GPL-3.0
Requires: arandr-bin = %{version}-%{release}
Requires: arandr-data = %{version}-%{release}
Requires: arandr-license = %{version}-%{release}
Requires: arandr-locales = %{version}-%{release}
Requires: arandr-man = %{version}-%{release}
Requires: arandr-python = %{version}-%{release}
Requires: arandr-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : docutils

%description
checklist before release:
* work on branch master
* set version in `setup.py` and `screenlayout/meta.py`
* make sure the latest NEWS entry matches
* commit as 'Ready for release ...'
* `git log --first-parent master > ChangeLog.new`
* `git checkout release`
* `git merge --no-ff master` (files may be modified in both: deleted in release, modified in master. the probably hould still be deleted.)
* `mv ChangeLog.new ChangeLog; git commit --amend -a` and set commit message to last NEWS entry
* `git tag $VERSION`
* `git archive $VERSION --prefix="arandr-$VERSION/" | gzip -9 > ../arandr_$VERSION.orig.tar.gz`
* `pristine-tar commit ../arandr_$VERSION.orig.tar.gz $VERSION`
* push to all mirrors, including tags
* notify maintainers

%package bin
Summary: bin components for the arandr package.
Group: Binaries
Requires: arandr-data = %{version}-%{release}
Requires: arandr-license = %{version}-%{release}

%description bin
bin components for the arandr package.


%package data
Summary: data components for the arandr package.
Group: Data

%description data
data components for the arandr package.


%package license
Summary: license components for the arandr package.
Group: Default

%description license
license components for the arandr package.


%package locales
Summary: locales components for the arandr package.
Group: Default

%description locales
locales components for the arandr package.


%package man
Summary: man components for the arandr package.
Group: Default

%description man
man components for the arandr package.


%package python
Summary: python components for the arandr package.
Group: Default
Requires: arandr-python3 = %{version}-%{release}

%description python
python components for the arandr package.


%package python3
Summary: python3 components for the arandr package.
Group: Default
Requires: python3-core

%description python3
python3 components for the arandr package.


%prep
%setup -q -n arandr-0.1.10
cd %{_builddir}/arandr-0.1.10

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1582846277
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/arandr
cp %{_builddir}/arandr-0.1.10/COPYING %{buildroot}/usr/share/package-licenses/arandr/8624bcdae55baeef00cd11d5dfcfa60f68710a02
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
%find_lang arandr

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/arandr
/usr/bin/unxrandr

%files data
%defattr(-,root,root,-)
/usr/share/applications/arandr.desktop

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/arandr/8624bcdae55baeef00cd11d5dfcfa60f68710a02

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/arandr.1.gz
/usr/share/man/man1/unxrandr.1.gz

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

%files locales -f arandr.lang
%defattr(-,root,root,-)

