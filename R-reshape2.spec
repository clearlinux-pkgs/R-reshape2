#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-reshape2
Version  : 1.4.4
Release  : 73
URL      : https://cran.r-project.org/src/contrib/reshape2_1.4.4.tar.gz
Source0  : https://cran.r-project.org/src/contrib/reshape2_1.4.4.tar.gz
Summary  : Flexibly Reshape Data: A Reboot of the Reshape Package
Group    : Development/Tools
License  : MIT
Requires: R-reshape2-lib = %{version}-%{release}
Requires: R-Rcpp
Requires: R-plyr
Requires: R-stringr
BuildRequires : R-Rcpp
BuildRequires : R-plyr
BuildRequires : R-stringr
BuildRequires : buildreq-R

%description
# reshape2
<!-- badges: start -->
[![R build status](https://github.com/hadley/reshape/workflows/R-CMD-check/badge.svg)](https://github.com/hadley/reshape/actions)
[![Codecov test coverage](https://codecov.io/gh/hadley/reshape/branch/master/graph/badge.svg)](https://codecov.io/gh/hadley/reshape?branch=master)
<!-- badges: end -->

%package lib
Summary: lib components for the R-reshape2 package.
Group: Libraries

%description lib
lib components for the R-reshape2 package.


%prep
%setup -q -c -n reshape2
cd %{_builddir}/reshape2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1589582246

%install
export SOURCE_DATE_EPOCH=1589582246
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
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
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library reshape2
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library reshape2
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc reshape2 || :


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
/usr/lib64/R/library/reshape2/NEWS.md
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
/usr/lib64/R/library/reshape2/tests/testthat.R
/usr/lib64/R/library/reshape2/tests/testthat/test-cast.r
/usr/lib64/R/library/reshape2/tests/testthat/test-margins.r
/usr/lib64/R/library/reshape2/tests/testthat/test-melt.r

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/reshape2/libs/reshape2.so
/usr/lib64/R/library/reshape2/libs/reshape2.so.avx2
/usr/lib64/R/library/reshape2/libs/reshape2.so.avx512
