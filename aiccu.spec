Summary:	AICCU - SixXS Automatic IPv6 Connectivity Client Utility
Summary(pl):	AICCU - Klient automatycznych po³±czeñ IPv6 z SixXS
Name:		aiccu
Version:	2005.01.31
Release:	0.2
License:	GPL
Group:		Networking/Utilities
URL:		http://www.sixxs.net/tools/aiccu/
Vendor:		SixXS
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Source0:	http://www.sixxs.net/archive/sixxs/aiccu/unix/%{name}_%{version}.tar.gz
# Source0-md5:	7c3da5feab3d59fb5a99a45203e0ca56
Patch0:		%{name}-makefile.diff
Patch1:		%{name}-RA.patch
Requires:	iproute2
Requires(post,preun):	chkconfig

%description
This client automatically gives one IPv6 connectivity without having
to manually configure interfaces etc. One does need a SixXS account
and at least a tunnel. These can be freely & gratis requested from the
SixXS website. For more information about SixXS check
http://www.sixxs.net

%description -l pl
Ten klient automatycznie pozwala na stworzenie po³±czenia IPv6 bez
konieczno¶ci rêcznej konfiguracji interfejsów itp. Potrzeba do tego
konta w serwisie SixXS oraz conajmniej tunelu. Mog± one byæ uzyskane
na stronie SixXS http://www.sixx.net, któr± odwied¼ w celu uzyskania
szczegó³ów.

%prep
%setup -q -n %{name}
%patch0 -p1
%patch1 -p1

%build
%{__make} RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

%post
#if [ "$1" = "1" ]; then
#	chkconfig --add aiccu
#fi

%preun
#if [ "$1" = "0" ]; then
#	service aiccu stop >/dev/null 2>&1
#	/sbin/chkconfig --del aiccu
#fi

%clean
make clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(600, root, root) %{_sysconfdir}/aiccu.conf
%doc doc/README doc/LICENSE
%attr(755,root,root) %{_sbindir}/aiccu
%attr(754,root,root) %config /etc/rc.d/init.d/aiccu
