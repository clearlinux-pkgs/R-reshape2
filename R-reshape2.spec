#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-reshape2
Version  : 1.4.1
Release  : 21
URL      : http://cran.r-project.org/src/contrib/reshape2_1.4.1.tar.gz
Source0  : http://cran.r-project.org/src/contrib/reshape2_1.4.1.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: R-Rcpp
Requires: R-plyr
Requires: R-stringr
Requires: R-testthat
BuildRequires : R-Rcpp
BuildRequires : R-plyr
BuildRequires : R-stringr
BuildRequires : R-testthat
BuildRequires : clr-R-helpers

%description
# Reshape2
[![Build Status](https://travis-ci.org/hadley/reshape.png)](https://travis-ci.org/hadley/reshape)

%prep
%setup -q -c -n reshape2

%build

%install
rm -rf %{buildroot}
export LANG=C
mkdir -p %{buildroot}/usr/lib64/R/library
R CMD INSTALL --install-tests --build  -l %{buildroot}/usr/lib64/R/library reshape2
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-codoc -l %{buildroot}/usr/lib64/R/library reshape2


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/reshape2/CITATION
/usr/lib64/R/library/reshape2/DESCRIPTION
/usr/lib64/R/library/reshape2/INDEX
/usr/lib64/R/library/reshape2/LICENSE
/usr/lib64/R/library/reshape2/Meta/Rd.rds
/usr/lib64/R/library/reshape2/Meta/data.rds
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
/usr/lib64/R/library/reshape2/libs/reshape2.so
/usr/lib64/R/library/reshape2/libs/symbols.rds