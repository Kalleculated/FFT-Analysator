**Correlation Function**:
The correlation function is used to investigate temporal relationships within a signal or between two signals. The autocorrelation function considers the investigation with one signal and is defined by:

$$
\psi_{xx}(\tau) = \lim_{T \to \infty} \frac{1}{T} \int_0^T x(t)x(t+\tau)dt.
$$

The function is symmetric (\(\psi_{xx}(\tau) = \psi_{xx}(-\tau)\)) due to the commutativity of the factors of the product in the integrand. For two different signals \(x\) and \(y\), the cross-correlation function can be calculated:

$$
\psi_{xy}(\tau) = \lim_{T \to \infty} \frac{1}{T} \int_0^T x(t)y(t+\tau)dt.
$$

The function does not have symmetry (\(\psi_{xy}(\tau) = \psi_{yx}(-\tau)\)).

**Power Spectral Density**:
The power spectral density (or simply, power spectrum) for a signal is referred to as the autoleistungsspektrum and indicates the distribution of the power of the signal across different frequencies and can be derived from the autocorrelation function:

$$
S_{xx}(f) = \int_{-\infty}^{+\infty} \psi(\tau)e^{-j2\pi f\tau}d\tau.
$$

The relationship between the correlation function and the power spectrum is thus given by Fourier transformation:

$$
\psi_{xx}(\tau) = \int_{-\infty}^{+\infty} S_{xx}(f)e^{j2\pi f\tau}df.
$$

Due to the properties of the Fourier transformation, the autoleistungsspektrum is also symmetric \(S_{xx}(-f) = S_{xx}(f)\). As with the autocorrelation function, only the one-sided spectrum is considered for physical relevance:

$$
G_{xx}(f) = 2S_{xx}(f), \quad f \geq 0.
$$

For two signals, the cross-power spectrum can be calculated:

$$
\underline{S}_{xy}(f) = \int_{-\infty}^{+\infty} \psi_{xy}(\tau)e^{-j2\pi f\tau}d\tau.
$$

The cross-power spectrum has the following properties:

$$
\underline{S}_{xy}(-f) = \underline{S}_{xy}^*(f) \quad \text{and} \quad \underline{S}_{xy}(f) = \underline{S}_{yx}^*(f).
$$

Here too, it makes sense to restrict the spectrum to positive frequencies, and one obtains for the one-sided spectrum \(\underline{G}_{xy} = 2\underline{S}_{xy}(f)\), \(f \geq 0\).

**For practical applications**, power spectra are calculated efficiently using Fourier transformation, exploiting the relationship between correlation functions and power spectra to compute the correlation functions. For a discrete time signal \(x_i(t)\), the Fourier transformation over an observation period \(0 \leq t \leq T\) is defined by:

$$
\underline{X}_i(f,T) = \int_0^T x_i(t)e^{-j2\pi ft}dt.
$$

With the magnitude square of the Fourier transform, the distribution of signal power over the frequencies \(f\) for \(x_i(t)\) can be indicated by:

$$
S_{xx}(f,T,i) = \frac{1}{T} | \underline{X}_i(f,T)|^2 = \frac{1}{T} \underline{X}_i(f,T)\underline{X}_i^*(f,T).
$$

By taking the expected value for all discrete values \(i\), the auto or cross-power spectrum can then be determined:

$$
G_{xx}(f) = 2 \cdot \lim_{T \to \infty} E(\underline{X}_i(f,T)\underline{X}_i^*(f,T)),
$$

$$
\underline{G}_{xy}(f) = 2 \cdot \lim_{T \to \infty} E(\underline{X}_i(f,T)\underline{Y}_i^*(f,T)).
$$

**Coherence**:
Coherence is a statistical measure for the linear relationship between two signals, can take values between \(0 \leq \gamma_{xy}^2 \leq 1\) and is calculated as follows:

$$
\gamma_{xy}^2(f) = \frac{| \underline{G_{xy}}(f)^2|}{G_{xx}(g)G_{yy}(f)}.
$$

**Frequency Response**:
The frequency response shows how a system processes signals of different frequencies. To account for the possibility of noise in the output or input signal, there are various approaches to provide a suitable estimate of the frequency response without systematic errors. A possible estimate based on the given power spectra is:

$$
\underline{H}_1(f) = \frac{\underline{G}_{xy}(f)}{G_{xx}(f)}.
$$

**Impulse Response**:
Frequency response and impulse response are linked via the Fourier transform. Thus, the impulse response, which describes the reaction of a physical system to a Dirac pulse, can be obtained from the inverse Fourier transformation of the frequency response.
