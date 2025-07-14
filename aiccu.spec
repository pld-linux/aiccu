Summary:	AICCU - SixXS Automatic IPv6 Connectivity Client Utility
Summary(pl.UTF-8):	AICCU - Klient automatycznych połączeń IPv6 z SixXS
Name:		aiccu
Version:	2007.01.15
%define		filever	20070115
Release:	3
License:	BSD
Group:		Networking/Utilities
Source0:	http://www.sixxs.net/archive/sixxs/aiccu/unix/%{name}_%{filever}.tar.gz
# Source0-md5:	c9bcc83644ed788e22a7c3f3d4021350
Patch0:		%{name}-makefile.diff
Patch1:		02_skip-strip.patch
Patch2:		03_no-quiet-gcc.patch
Patch3:		05_spelling-error.patch
Patch4:		06_syslog_openlog.patch
Patch5:		07_allow_tunnels.patch
Patch6:		08_setup_script.patch
Patch7:		09_binutils_gold.patch
Patch8:		10_gnutls34.patch
Patch9:		11_gnutls-cleanup.patch
Patch10:	12_memset-sizeof.patch
Patch11:	13_autotest_description.patch
URL:		http://www.sixxs.net/tools/aiccu/
BuildRequires:	gnutls-devel
#Requires(post,preun):	/sbin/chkconfig
Requires:	gnutls
Requires:	iproute2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This client automatically gives one IPv6 connectivity without having
to manually configure interfaces etc. One does need a SixXS account
and at least a tunnel. These can be freely & gratis requested from the
SixXS website. For more information about SixXS check
<http://www.sixxs.net/>.

%description -l pl.UTF-8
Ten klient automatycznie pozwala na stworzenie połączenia IPv6 bez
konieczności ręcznej konfiguracji interfejsów itp. Potrzeba do tego
konta w serwisie SixXS oraz co najmniej tunelu. Mogą one być uzyskane
na stronie SixXS <http://www.sixx.net/>, na której można znaleźć
więcej szczegółów.

%prep
%setup -q -n %{name}
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
%patch -P4 -p1
%patch -P5 -p1
%patch -P6 -p1
%patch -P7 -p1
%patch -P8 -p1
%patch -P9 -p1
%patch -P10 -p1
%patch -P11 -p1

%build
%{__make} \
	RPM_OPT_FLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
#if [ "$1" = "1" ]; then
#	/sbin/chkconfig --add aiccu
#fi

%preun
#if [ "$1" = "0" ]; then
#	/etc/rc.d/init.d/aiccu stop >/dev/null 2>&1
#	/sbin/chkconfig --del aiccu
#fi

%files
%defattr(644,root,root,755)
%doc doc/README doc/LICENSE
%attr(755,root,root) %{_sbindir}/aiccu
%attr(600,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/aiccu.conf
%attr(754,root,root) %config(noreplace) %verify(not md5 mtime size) /etc/rc.d/init.d/aiccu
