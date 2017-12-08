#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-reshape2
Version  : 1.4.2
Release  : 44
URL      : http://cran.r-project.org/src/contrib/reshape2_1.4.2.tar.gz
Source0  : http://cran.r-project.org/src/contrib/reshape2_1.4.2.tar.gz
Summary  : Flexibly Reshape Data: A Reboot of the Reshape Package
Group    : Development/Tools
License  : MIT
Requires: R-reshape2-lib
Requires: R-Rcpp
Requires: R-plyr
BuildRequires : R-Rcpp
BuildRequires : R-plyr
BuildRequires : clr-R-helpers

%description
# Reshape2
[![Build Status](https://travis-ci.org/hadley/reshape.png)](https://travis-ci.org/hadley/reshape)

%package lib
Summary: lib components for the R-reshape2 package.
Group: Libraries

%description lib
lib components for the R-reshape2 package.


%prep
%setup -q -c -n reshape2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1502419478

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1502419478
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library reshape2
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library reshape2
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library reshape2
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/reshape2/CITATION
/usr/lib64/R/library/reshape2/DESCRIPTION
/usr/lib64/R/library/reshape2/INDEX
/usr/lib64/R/library/reshape2/LICENSE
/usr/lib64/R/library/reshape2/Meta/Rd.rds
/usr/lib64/R/library/reshape2/Meta/data.rds
/usr/lib64/R/library/reshape2/Meta/features.rds
/usr/lib64/R/library/reshape2/Meta/hsearch.rds
/usr/lib64/R/library/reshape2/Meta/links.rds
/usr/lib64/R/library/reshape2/Meta/nsInfo.rds
/usr/lib64/R/library/reshape2/Meta/package.rds
/usr/lib64/R/library/reshape2/NAMESPACE
/usr/lib64/R/library/reshape2/R/reshape2
/usr/lib64/R/library/reshape2/R/reshape2.rdb
/usr/lib64/R/library/reshape2/R/reshape2.rdx
/usr/lib64/R/library/reshape2/data/Rdata.rdb
/usr/lib64/R/library/reshape2/data/Rdata.rds
/usr/lib64/R/library/reshape2/data/Rdata.rdx
/usr/lib64/R/library/reshape2/help/AnIndex
/usr/lib64/R/library/reshape2/help/aliases.rds
/usr/lib64/R/library/reshape2/help/paths.rds
/usr/lib64/R/library/reshape2/help/reshape2.rdb
/usr/lib64/R/library/reshape2/help/reshape2.rdx
/usr/lib64/R/library/reshape2/html/00Index.html
/usr/lib64/R/library/reshape2/html/R.css
/usr/lib64/R/library/reshape2/libs/symbols.rds

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/reshape2/libs/reshape2.so
/usr/lib64/R/library/reshape2/libs/reshape2.so.avx2
