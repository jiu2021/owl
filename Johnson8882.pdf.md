![Image](https://storage.googleapis.com/chunkr-prod-bucket/84b768a3-ce8f-4a71-8245-8c88c8639b23/f1ded069-e7ec-4fb2-a7ea-5649281478c8/images/060b30bc-fd60-4f4e-8367-390b046ffcc3.jpg?x-id=GetObject&response-content-disposition=inline&response-content-encoding=utf-8&response-content-type=image%2Fjpeg&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=GOOG1EBMQ2D33SPB3VQ4MMVJEKXWQFNK5WS57JRFVYUSD3ZCA76OC3B74IG7C%2F20250528%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20250528T033640Z&X-Amz-Expires=3600&X-Amz-SignedHeaders=host&X-Amz-Signature=feb1241680458fee9ccf20a598bd11fe844d5f7e482daba2b275e1e82b373c92)

# The Original Michaelis Constant: Translation of the 1913 Michaelis- Menten Paper

Kenneth A. Johnson *** and Roger S. Goody*

Department of Chemistry and Biochemistry, Institute for Cell and Molecular Biology, 2500 Speedway, The University of Texas, Austin, Texas 78735, United States

Department of Physical Biochemistry, Max-Planck Institute of Molecular Physiology, Otto-Hahn-Strasse 11, 44227 Dortmund, Germany

## S Supporting Information

ABSTRACT: Nearly 100 years ago Michaelis and Menten Michaelis-Menten Data Sucrose Invertase Fructose + Glucose published their now classic paper [Michaelis, L., and Menten, 3º M. L. (1913) Die Kinetik der Invertinwirkung. Biochem. Z. 49, 1913 1.0 2-0.16 7-0.333 2011 3-0.0833 333-369] in which they showed that the rate of an enzyme- 0.8 catalyzed reaction is proportional to the concentration of the 2° 4-0.0426 0.6 enzyme-substrate complex predicted by the Michaelis- Menten equation. Because the original text was written in 1º 0.4 - 0.0208 Ratio P/S. German yet is often quoted by English-speaking authors, we undertook a complete translation of the 1913 publication, 6-0.0204 0.2 Optical Rotation, degrees 7 -0.0052 which we provide as Supporting Information. Here we 0 0 0 50 100 150 0 Time, m Time. m 50 100 150 200 250 introduce the translation, describe the historical context of the work, and show a new analysis of the original data. In doing so, we uncovered several surprises that reveal an interesting glimpse into the early history of enzymology. In particular, our reanalysis of Michaelis and Menten's data using modern computational methods revealed an unanticipated rigor and precision in the original publication and uncovered a sophisticated, comprehensive analysis that has been overlooked in the century since their work was published. Michaelis and Menten not only analyzed initial velocity measurements but also fit their full time course data to the integrated form of the rate equations, including product inhibition, and derived a single global constant to represent all of their data. That constant was not the Michaelis constant, but rather Vmax/Km, the specificity constant times the enzyme concentration (kcat/Km × Eo).

I n 1913 Leonor Michaelis and Maud Leonora Menten published their now classic paper, Die Kinetik der Invertinwerkung.1 They studied invertase, which was so named because its reaction results in the inversion of optical rotation from positive for sucrose to a net negative for the sum of fructose plus glucose.

invertase sucrose -> fructose + glucose

After receiving her M.D. degree in 1911 at the University of Toronto, Maud Leonora Menten (1879-1960) worked as a research assistant in the Berlin laboratory of Leonor Michaelis (1875-1949). She monitored the rate of the invertase- catalyzed reaction at several sucrose concentrations by careful measurement of optical rotation as a function of time, following the reaction to completion. Their goal was to test the theory that "invertase forms a complex with sucrose that is very labile and decays to free enzyme, glucose and fructose", leading to the prediction that "the rate of inversion must be proportional to the prevailing concentration of sucrose-enzyme complex." Michaelis and Menten recognized that the products of the reaction were inhibitory, as known from prior work by Henri.2 Although most enzyme kinetic studies at the time had sought an integrated form of the rate equations, Michaelis and Menten

circumvented product inhibition by performing initial velocity measurements where they would only "need to follow the inversion reaction in a time range where the influence of the cleavage products is not noticeable. The influence of the cleavage products can then be easily observed in separate experiments." Michaelis and Menten performed initial velocity measurements as a function of variable sucrose concentration and fit their data on the basis of the assumption that the binding of sucrose was in equilibrium with the enzyme and the postulate that the rate of the reaction was proportional to the concentration of the enzyme-substrate complex. By showing that the sucrose concentration dependence of the rate followed the predicted hyperbolic relationship, they provided evidence to support the hypothesis that enzyme catalysis was due to formation of an enzyme-substrate complex, according to the now famous Michaelis-Menten equation, and found, "for the first time, a picture of the magnitude of the affinity of an enzyme for its substrate." They also derived expressions for competitive inhibition and quantified the effects of products on the rates of reaction to obtain estimates for the dissociation

| Received: | August 12, 2011 |
| Revised: | August 30, 2011 |
| Published: | September 2, 2011 |

![Image](https://storage.googleapis.com/chunkr-prod-bucket/84b768a3-ce8f-4a71-8245-8c88c8639b23/f1ded069-e7ec-4fb2-a7ea-5649281478c8/images/88cf525e-bacb-4c23-8772-f10577e73010.jpg?x-id=GetObject&response-content-disposition=inline&response-content-encoding=utf-8&response-content-type=image%2Fjpeg&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=GOOG1EBMQ2D33SPB3VQ4MMVJEKXWQFNK5WS57JRFVYUSD3ZCA76OC3B74IG7C%2F20250528%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20250528T033640Z&X-Amz-Expires=3600&X-Amz-SignedHeaders=host&X-Amz-Signature=b5623f25312e37f772a36c9480cf9a89ad66471c22606eae72fa9d9a8ed534b4)

constants for fructose and glucose. As a final, comprehensive test of their model, they analyzed full time course kinetic data based upon the integrated form of the rate equations, including product inhibition. Thus, as we describe below, they accomplished a great deal more than is commonly recognized.

## NOTES ON THE TRANSLATION

The style of the paper is surprisingly colloquial, making us realize how formal we are in our present writing. In translating the paper, which we provide here as Supporting Information, we have attempted to retain the voice of the original, while using terms that will be familiar to readers in the 21st Century. Michaelis and Menten referred to the enzyme as the "ferment", but we adopt the word "enzyme" on the basis of contemporaneous papers written in English. Their reference to initial velocity literally translates as the "maximum velocity of fission", which we interpret to mean the maximum velocity during the initial phase of the reaction before the rate begins to taper off because of substrate depletion and product inhibition; therefore, we have adopted the conventional "initial rate" terminology. The term Restdissoziationskurve, which is not commonly used, posed some problems in translation. We chose to rely upon the context in which it was used relative to mathematical expressions describing the fractional saturation of an acid as a function of pH, implying the meaning "association curve" in modern terms.

By modern standards there are a number of idiosyncrasies, including the lack of dimensions on reported parameters and some very loose usage of concepts. For example, on page 23 of our translation, the authors attribute the inhibitory effect of ethanol, with an apparent Ka of 0.6 M, as being entirely due to a change in the character of the solvent and accordingly assign a value of co to Kalcohol; however, we now believe that for most enzymes a solution containing 5% alcohol is not inhibitory due to solvent effects. A general feature of the paper is an inexact use of the terms quantity, amount, and concentration. In most cases, the authors mean concentration when they say amount. In the tables they used the unit n, but in the text they generally used N to represent concentration. Throughout the translation, we have converted to the use of M to designate molar concentrations. Of course, Michaelis and Menten had no way of knowing the enzyme concentration in their experiments, so all references were to relative amounts of enzyme added to the reaction mixtures. Surprisingly lacking was any mention of the source of the enzyme or the methods used for its preparation.

We have tried to reproduce the overall feeling of the paper with approximately the same page breaks and layout of text and figures. We have retained the original footnotes at the bottom of each page and interspersed our own editorial comments. In general, we translated the paper literally but corrected two minor math errors (sign and subscript), which were not propagated in subsequent equations in the original text. All of the original data for each of the figures were provided in tables, a useful feature lacking in today's publications. The availability of the original data allowed us to redraw figures and reanalyze the results using modern computational methods. We have attempted to recreate the style of the original figures, with one exception. In Figures 1-3, individual data points were plotted using a small x with an adjacent letter or number to identify the data set. In attempting to recreate this style, we found the labeling to be unreliable and ambiguous, so we have resorted to the use of modern symbols.

## HISTORICAL PERSPECTIVE

Perhaps the unsung hero of the early history of enzymology is Victor Henri, who first derived an equation predicting the relationship between rate and substrate concentration based upon a rational model involving the formation of a catalytic enzyme-substrate complex.2 However, as Michaelis and Menten point out, Henri made two crucial mistakes, which prevented him from confirming the predicted relationship between rate and substrate concentration. He failed to account for the slow mutarotation of the products of the reaction (equilibration of the a and ß anomers of glucose), and he neglected to control pH. Thus, errors in his data precluded an accurate test of the theory. Otherwise, we would probably be writing about the Henri equation.

As they are usually credited, Michaelis and Menten measured the initial velocity as a function of sucrose concentration and derived an equation that approximates the modern version of the Michaelis-Menten equation:

v = CØ [S] + k [S]

where CD = Vmax + is the total enzyme concentration, and k = Ks, the dissociation constant of the sucrose-enzyme complex. In this expression, C is kcat multiplied by a factor to convert the change in optical rotation to the concentration of substrate converted to product.

Michaelis and Menten overlooked the obvious double- reciprocal plot as a means of obtaining a linear extrapolation to an infinite substrate concentration. Rather, Michaelis relied upon his experience in analysis of pH dependence (although the term, pH, had not yet been defined). They replotted their data as rate versus the log of substrate concentration, in a form analogous to the Henderson-Hasselbalch equation for pH dependence, to be published four years later.3 Michaelis and Menten then followed a rather complicated procedure for estimating Ks from the data without knowing the maximum velocity of the reaction. They derived an expression defining the slope of the plot of the initial rate against the log of the substrate concentration at V/2 [in their terminology V = v/ (CD), expressed as a fraction of the maximum velocity]. They reasoned that the curve of V versus log[S] should be approximately linear around V/2 with a slope of 0.576. The scale of the ordinate of a plot of rate versus log[S] was then adjusted to make the slope truly equal to 0.576, and because the adjusted curve should saturate at V = 1, they could then read off the value of log[S] at V = 0.5 to determine Ks. This lengthy procedure allowed normalization of their data to afford extrapolation to substrate saturation to estimate Vmax and thus determine the Ks for sucrose. Having seen Michaelis's mathematical prowess, which is evident in this paper and a subsequent book,4 we were surprised that he did not think of linearizing the equation to give

1 _ 1 k +

v CD CD[S]

Twenty years later Lineweaver and Burk would discover the utility of the double-reciprocal plot, and their 1934 paper would go on to be the most cited in the history of the Journal of the American Chemical Society, with more than 11000 citations (Lineweaver died in 2009 at the age of 101).

Michaelis and Menten assumed equilibrium binding of sucrose to the enzyme during the course of the reaction.

Within a year Van Slyke and Cullen6 published a derivation in which binding of substrate to the enzyme and product release were both considered to be irreversible reactions, producing a result identical to the Michaelis-Menten equation. Their focus, like that of Michaelis and Menten, was on the integrated form of the rate equations and the fitting of data from the full time course of the reaction, and they noted some inconsistencies in their attempts to fit data as the reaction approached equilibrium. It was not until 12 years later in 1925 that Briggs and Haldane7 introduced the steady state approximation and provided arguments supporting the validity of initial velocity measurements, thereby eliminating the need to assume that the substrate binding was in rapid equilibrium or irreversible. They reasoned that because the concentration of enzyme was negligible relative to the concentration of substrate, the rate of change in the concentration of the enzyme-substrate complex, "except for the first instant of the reaction", must also be negligible compared with the rates of change in the concentrations of substrate and product. This provided the justification for the steady state approximation. Modeling sucrose binding as an equilibrium in the derivation published by Michaelis and Menten was probably correct for the binding of sucrose to invertase, although, in fitting of steady state kinetic data to extract kcat and kcat/Km values, the details regarding the intrinsic rate constants governing substrate binding need not be known and do not affect the outcome, a fact recognized by Briggs and Haldane. The Briggs and Haldane derivation based upon the steady state approximation is used in biochemistry textbooks to introduce the Michaelis-Menten equation. Perhaps our current usage of terms came into vogue after the reference by Briggs and Haldane to "Michaelis and Menten's equation" and "their constant Ks".

## PRODUCT INHIBITION AND THE INTEGRATED RATE EQUATION

The analysis by Michaelis and Menten went far beyond the initial velocity measurements for which their work is most often cited. Rather, in what constitutes a real tour de force of the paper, they fit their full time course data to the integrated form of the rate equation while accounting for inhibition by the products of the reaction. They showed that all of their data, collected at various times after the addition of various concentrations of sucrose, could be analyzed to derive a single constant. In their view, this analysis confirmed that their approach was correct, based upon estimates of the dissociation constants for sucrose, glucose, and fructose derived from the initial velocity measurements. In retrospect, their analysis can now be recognized as the first global analysis of full time course kinetic data! The constant derived by Michaelis and Menten provided a critical test of their new model for enzyme catalysis, but it was not the Michaelis constant (Km). Rather, they derived Vmax/Km, a term we now describe as the specificity constant, kcat/Km, multiplied by the enzyme concentration, which, of course, was unknown to them.

Here, we show a brief derivation of the rate equations published by Michaelis and Menten, but with terms translated to be more familiar to readers today, with the exception that we retain the term "Const" to describe their new constant, and we show how they analyzed their data globally to extract a single kinetic parameter from their entire data set. Moreover, we show that globally fitting their data using modern computational methods based upon numerical integration of rate equations

gives essentially the same result produced by Michaelis and Menten nearly a century ago.

Michaelis and Menten tested the postulate that the rate of an enzyme-catalyzed reaction could be described by a constant term (c) multiplied by the concentration of the enzyme- substrate complex using the following model.

Ks E+SES-E+G+F C

dG dF dt dt v= == == c × ES Eo = E + ES V = cEo CS = DE LOS + Ks S + Ks S

Michaelis and Menten showed that the rate was proportional to the amount of enzyme (ferment) added to the reaction mixture, but they had no means of determining the molar enzyme concentration. Today, we recognize that c = kcat and C = Vmax although each term contained a factor to convert concentration units to degrees of optical rotation in their measurements. Subsequently, they used a conversion factor to calculate the fraction of substrate converted to product in fitting their data to the integrated form of the rate equation, as described below. Ks is equal to Km (the Michaelis constant), although it was defined as the equilibrium dissociation constant for sucrose. Michaelis and Menten went beyond this simple analysis and realized that the binding of the products of the reaction, fructose (F) and glucose (G), competes with the binding of sucrose and that a full analysis of the reaction time course would have to take product inhibition into account based upon a more complete model shown below.

E+S=ES-E+F+G Ks KF c

E + F=EF KG E + SEG

E + SEG

The dissociation constants for sucrose, fructose, and glucose were estimated from initial velocity measurements treating fructose and glucose as competitive inhibitors to give

Ks = 16.7 mM KF = 58.8 mM KG = 91 mM E = E0 - ES - EF - EG (mass balance)

Solving these equations simultaneously yielded

ES = S + Ks(1 + F/KF + G/KG) SE0

where ES, S, F, and G represent the time-dependent concentrations of the enzyme-sucrose complex, sucrose, fructose, and glucose, respectively. According to their postulate, the rate of reaction was proportional to the ES concentration:

v = = = = = X ES dG dt dF dt

dt

CS

V= S + Ks(1 + F/KF + G/KG)

where C = cE0. This is the now familiar form of the equation for competitive enzyme inhibition, where the terms F/KF and G/ KG in the denominator account for product inhibition. Although the concept of competitive inhibition had not yet been formally defined, it is clearly represented here mathemati- cally.

Michaelis and Menten reasoned that if their postulate was correct, then they would be able to fit the full time dependence of the reaction at various sucrose concentrations to derive a single constant, C, based upon the known values of Ks, KF, and KG. Integration of the rate equation requires including mass balance terms to reduce the equation to a form with a single variable for the concentration of S, F, or G.

S = So - F F = G dF

== [C(S) - F)] dt /[So- F + Ks(1 + F/KF + G/KG)] dF

== [C(S) - F)] dt /[So + Ks- FKs(1/Ks-1/KF-1/KG)] C differential equation was then integrated to

This yield

Const =

Ks

=

t + So

F t 1

So

KF

KF + 1 KG 1

× In So So - F )

1 Ks S

1 KG )

This equation allowed the constant term (Const = C/Ks) to be calculated from measurements of the concentration of product (F) as a function of time (t) at various starting concentrations of sucrose, S0. Michaelis and Menten converted their optical rotation data to obtain the fraction of product formed relative to starting substrate concentration, [P]/[S ], as illustrated in Table 1. They showed that, indeed, the constant term, C/Ks, was "very similar in all experiments and despite small variation shows no tendency for systematic deviation neither with time nor with sugar concentration, so that we can conclude that we can conclude that the value is reliably constant."

This extraordinary analysis allowed fitting of the full time course of product formation to the integrated form of the rate equation to extract a single unknown constant that accounts for all of the data. In doing so, Michaelis and Menten demonstrated that the variation in the rate of turnover as a function of time and substrate concentration could be understood as a constant defining the rate of product formation based upon the calculated concentration of the ES complex. This is a remarkable contribution. However, it should be noted that the constant derived by Michaelis and Menten in fitting their data was not the Michaelis constant. Rather, in terms used today, they fit their data to the constant C/Ks = (kcat/Km) E0, the specificity constant times the enzyme concentration. This was as far as they could take their analysis, because they had no way of knowing the enzyme concentration; the exact nature and molecular weight of the enzyme were unknown at the time.

_Table 1. Michaelis-Menten Global Data Fittingª_

| Time (min) | [P]/[S<sub>o</sub>] | Const |
|---|---|---|
| 7 | 0.0164 | 0.0496 |
| 14 | 0.0316 | 0.0479 |
| 26 | 0.0528 | 0.0432 |
| 49 | 0.0923 | 0.0412 |
| 75 | 0.1404 | 0.0408 |
| 117 | 0.2137 | 0.0407 |
| 1052 | 0.9834 | [0.0498] |

| Time (min) | [P]/[S<sub>o</sub>] | Const |
|---|---|---|
| 8 | 0.0350 | 0.0444 |
| 16 | 0.0636 | 0.0446 |
| 28 | 0.1080 | 0.0437 |
| 52 | 0.1980 | 0.0444 |
| 82 | 0.3000 | 0.0445 |
| 103 | 0.3780 | 0.0454 |

| Time (min) | [P]/[S<sub>o</sub>] | Const |
|---|---|---|
| 49.5 | 0.352 | 0.0482 |
| 90.0 | 0.575 | 0.0447 |
| 125.0 | 0.690 | 0.0460 |
| 151.0 | 0.766 | 0.0456 |
| 208.0 | 0.900 | 0.0486 |

| Time (min) | [P]/[S<sub>o</sub>] | Const |
|---|---|---|
| 10.25 | 0.1147 | 0.0406 |
| 30.75 | 0.3722 | 0.0489 |
| 61.75 | 0.615 | 0.0467 |
| 90.75 | 0.747 | 0.0438 |
| 112.70 | 0.850 | 0.0465 |
| 132.70 | 0.925 | 0.0443 |
| 154.70 | 0.940 | 0.0405 |

| Time (min) | [P]/[S<sub>o</sub>] | Const |
|---|---|---|
| 17 | 0.331 | 0.0510 |
| 27 | 0.452 | 0.0464 |
| 38 | 0.611 | 0.0500 |
| 62 | 0.736 | 0.0419 |
| 95 | 0.860 | [0.058] |
| 1372 | 0.990 |  |

"Const mean value = 0.0454 min-1. This reproduces the data from the last (unnumbered) table in ref 1. Michaelis and Menten analyzed these data using the integrated form of the rate equations to compute a single constant (Const = C/Ks), as described in the text. We fit these data globally on the basis of numerical integration of the rate equations to give the results shown in Figure 1.

Their data fitting provided an average C/Ks value of 0.0454 ± 0.0032 min-1, from which we can calculate Vmax = kcatEo = 0.76 ± 0.05 mM/min based upon their reported Ks value of 16.7 mM.

## COMPUTER ANALYSIS

Today, we can fit the original Michaelis-Menten data globally on the basis of numerical integration of the rate equations and no simplifying assumptions. Figure 1 shows the global fit of the data from the Michaelis-Menten paper (Table 1) obtained using the KinTek Explorer simulation program.8,9 The data were fit to a model in which S, F, and G each bind to the

+ 1

![Image](https://storage.googleapis.com/chunkr-prod-bucket/84b768a3-ce8f-4a71-8245-8c88c8639b23/f1ded069-e7ec-4fb2-a7ea-5649281478c8/images/1714ebdb-9133-4f1c-a2ac-f58894b4e1d9.jpg?x-id=GetObject&response-content-disposition=inline&response-content-encoding=utf-8&response-content-type=image%2Fjpeg&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=GOOG1EBMQ2D33SPB3VQ4MMVJEKXWQFNK5WS57JRFVYUSD3ZCA76OC3B74IG7C%2F20250528%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20250528T033640Z&X-Amz-Expires=3600&X-Amz-SignedHeaders=host&X-Amz-Signature=9cff19f6cf5e3f8fff16943e410b4c3e6c68515fc566dee7eb2a6bd2108e25b0)

_Figure 1. Global fit to the data of Michaelis and Menten. The data from Michaelis and Menten (reproduced in Table 1) were fit by simulation using KinTek Explorer9 with the only variable being kcatE0 to get the smooth lines; an arbitrary, low enzyme concentration was chosen to perform the simulation. Data are for starting concentrations of sucrose of 20.8 (A), 41.6 (V), 83 (+), 167 (), and 333 mM () from Table 1. Data at times longer than 250 min were included in the fit but are not displayed in the figure. The dashed lines show the kinetics predicted if product inhibition is ignored._

enzyme in a rapid equilibrium reaction using dissociation constants reported by Michaelis and Menten. The data were fit to a single kinetic constant (kcatE0 = 0.80 ± 0.02 mM/min). The global (average) value achieved by Michaelis and Menten (0.76 ± 0.05 mM/min) equals what can be derived today with the most advanced computer simulation software and stands as a testament to the precision of Maud Leonora Menten and Leonor Michaelis' measurements and their care in performing the calculations by hand.

Computer simulation can also be used to show how much product inhibition contributed to the time dependence of the reaction. The dashed lines in Figure 1 show the predicted time course assuming no product inhibition. Clearly, the rebinding of product to the enzyme makes a significant contribution to the time course. Perhaps Michaelis and Menten recognized this fact when they first attempted to fit their data to the integrated rate equation based on a simpler model and then realized that they must include competitive product inhibition. Further analysis by numerical integration also supports the conclusion of Michaelis and Menten that there is no significant accumulation of a ternary EFG complex based upon the postulate of noninteracting sites, fast product release, and the measured Ka values.

In the past century, enzyme kinetic analysis has followed the use of the steady state approximation, allowing initial velocity data to be fit using simple algebraic expressions. Michaelis and Menten set a high standard for comprehensive data fitting, and their pioneering work must now be considered a the forerunner to modern global data fitting. Work in enzymology during the first two decades of the 20th Century by Henri, Michaelis and Menten, and Van Slyke and Cullen was focused on finding the integrated form of the rate equations to account for the full progress curves of enzyme-catalyzed reactions. That approach is complicated by the assumptions necessary to derive a mathematical equation describing the full time course, namely, the assumption that the substrate concentration was always much greater than the enzyme concentration and the need for prior knowledge of the nature and KI values for product inhibition. Michaelis and Menten and Briggs and Haldane provided the simple solution to the problem by showing how initial velocity measurements during a steady state that exists

prior to significant substrate depletion can be used to derive kcat and Km for substrate turnover and K values for product inhibition. Lineweaver and Burk provided a simple graphical analysis to parse the kinetic data based upon a double- reciprocal plot. This type of analysis dominated enzymology for most of the 20th Century. Analysis by numerical integration of rate equations (also known as computer simulation) has eliminated the need for simplifying assumptions to afford quantitative analysis of full progress curves, as pioneered by Carl Frieden.1º One can now derive steady state kinetic parameters and product inhibition constants by fitting full time course data directly using computer simulation, "bypassing the laborious initial rate analysis. It is perhaps a testament to the early work in enzymology that only in the first decade of the 21st Century with the advent of fast personal computers and optimized algorithms that global data analysis of full progress curves has finally come of age.

It is also interesting to note that the original Michaelis constant, the one derived by Michaelis and Menten in analyzing their full time course data globally, was actually the specificity constant (kcat/Km) multiplied by the enzyme concentration, which was unknown at the time. We now recognize the specificity constant as the most important steady state kinetic parameter in that it defines enzyme specificity, efficiency, and proficiency.12 In contrast, the constant attributed to Michaelis, Km is less important in enzymology and quite often is misinterpreted. It is perhaps the case that the use of Km gained prominence because it could be measured without knowing the enzyme concentration and could be derived from any arbitrary rate measurements without the need to convert to units of concentration. Today, enzymologists generally regard kcat and kcat/Km as the two primary steady state kinetic parameters and think that Km is simply a ratio of kcat and kcat/Km. This view certainly generates less confusion than attempts to interpret Km without additional mechanistic information.13 In terms of smaller errors in estimating the specificity constant and a more realistic representation of the kinetics of enzyme-catalyzed reactions, a better form of the Michaelis-Menten equation would be

v = 1+(km/kcat)[S] km[S]

where km is the specificity constant, using a lowercase k to designate a kinetic rather than a pseudoequilibrium constant. We could perhaps refer to km to as the Menten constant.

## SUMMARY

Nearly a century after the original publication, the work of Michaelis and Menten stands up to the most critical scrutiny of informed hindsight. It is only unfortunate that the term Michaelis constant was not attributed to kcat/Km, which was derived as the constant in their "global" data analysis, rather than the Km term. For the past century and certainly for the next, enzymologists continue to work toward the goal, stated by Michaelis and Menten in their opening paragraph, of "achieving the final aim of kinetic research; namely, to obtain knowledge of the nature of the reaction from a study of its progress."

## ASSOCIATED CONTENT

## S Supporting Information

Full text of the German to English translation of the original 1913 Michaelis and Menten paper. This material is available free of charge via the Internet at http://pubs.acs.org.

## AUTHOR INFORMATION

## Corresponding Author

*Department of Chemistry and Biochemistry, Institute for Cellular and Molecular Biology, The University of Texas, Austin, TX 78712. E-mail: kajohnson@mail.utexas.edu. Phone: (512) 471-0434. Fax: (512) 471-0435.

## Funding

Supported by a grant from The Welch Foundation (F-1604) and the National Institutes of Health (GM084741) to K.A.J. and by a grant from the Deutsche Forschungsgemeinschaft (SFB642, Project A4) to R.S.G.

## ACKNOWLEDGMENTS

KinTek Corp. provided KinTek Explorer.

## REFERENCES

(1) Michaelis, L., and Menten, M. L. (1913) Die Kinetik der Invertinwirkung. Biochem. Z. 49, 333-369.

(2) Henri, V. (1903) Lois générales de l'action des diastases, Hermann, Paris.

(3) Hasselbalch, K. A. (1917) Die Berechnung der Wasserstoffzahl des Blutes aus der freien und gebundenen Kohlensäure desselben, und die Sauerstoffbindung des Blutes als Funktion der Wasserstoffzahl. Biochem. Z. 78, 112-144.

(4) Michaelis, L. (1922) Einführung in die Mathematik, Springer, Berlin.

(5) Lineweaver, H., and Burk, D. (1934) The determination of enzyme dissociation constants. J. Am. Chem. Soc. 56, 658-666.

(6) Van Slyke, D. D., and Cullen, G. E. (1914) The mode of action of urease and of enzymes in general. J. Biol. Chem. 19, 141-180.

(7) Briggs, G. E., and Haldane, J. B. S. (1925) A note on the kinetics of enzyme action. Biochem. J. 19, 338-339.

(8) Johnson, K. A., Simpson, Z. B., and Blom, T. (2009) FitSpace Explorer: An algorithm to evaluate multidimensional parameter space in fitting kinetic data. Anal. Biochem. 387, 30-41.

(9) Johnson, K. A., Simpson, Z. B., and Blom, T. (2009) Global Kinetic Explorer: A new computer program for dynamic simulation and fitting of kinetic data. Anal. Biochem. 387, 20-29.

(10) Barshop, B. A., Wrenn, R. F., and Frieden, C. (1983) Analysis of numerical methods for computer simulation of kinetic processes: Development of KINSIM-a flexible, portable system. Anal. Biochem. 130, 134-145.

(11) Johnson, K. A. (2009) Fitting enzyme kinetic data with KinTek Global Kinetic Explorer. Methods Enzymol. 467, 601-626.

(12) Miller, B. G., and Wolfenden, R. (2002) Catalytic proficiency: The unusual case of OMP decarboxylase. Annu. Rev. Biochem. 71, 847- 885.

(13) Tsai, Y. C., and Johnson, K. A. (2006) A new paradigm for DNA polymerase specificity. Biochemistry 45, 9675-9687.

# Die Kinetik der Invertinwirkung

Von L. Michaelis and Miss Maud L. Menten (Received 4 February 1913.) With 19 Figures in Text.

# The Kinetics of Invertase Action

translated by

Roger S. Goody and Kenneth A. Johnson2

The kinetics of enzyme3) action have often been studied using invertase, because the ease of measuring its activity means that this particular enzyme offers especially good prospects of achieving the final aim of kinetic research, namely to obtain knowledge on the nature of the reaction from a study of its progress. The most outstanding work on this subject is from Duclaux4), Sullivan and Thompson5), A.J. Brown6) and in particular V. Henri7). Henri's investigations are of particular importance since he succeeded, starting from rational assumptions, in arriving at a mathematical description of the progress of enzymatic action that came quite near to experimental observations in many points. We start from Henri's considerations in the present work. That we have gone to the lengths of reexamination of this work arises from the fact that Henri did not take into account two aspects, which must now be taken so seriously that a new investigation is warranted. The first point to be taken into account is the hydrogen ion concentration, the second the mutarotation of the sugar(s).

The influence of the hydrogen ion concentration has been clearly demonstrated by the work of Sörensen8) and of Michaelis and Davidsohn9). It would be a coincidence if Henri in all his experiments, in which he did not consider the hydrogen ion concentration, had worked at the same hydrogen ion concentration. This has been conveniently addressed in our present contribution by addition of an acetate mixture that produced an H+-concentration of 2:10-5 M1º)

1 Director of the Dept. of Physical Biochemistry, Max-Planck Institute of Molecular Physiology, Otto-Hahn-Strasse 11, 44227 Dortmund, Germany. Email: roger.goody@mpi-dortmund.de

2 Professor of Biochemistry, Institute for Cell and Molecular Biology, 2500 Speedway, University of Texas, Austin, TX 78735 USA. Email: kajohnson@mail.utexas.edu

3 Michaelis and Menten use the word "ferment", but we adopt the word "enzyme" following papers from the same period written in English.

4 Duclaux, Traité de Microbiologie 0899, Bd. II.

5 O. Sullivan and Thompson, J. Chem. Soc. (1890) 57, 834.

6 A. J. Brown, J. Chem. Soc. (1902), 373.

7 Victor Henri, Lois générales de l'action des diastases, Paris (1903).

8 S. P. L. Sörensen, Enzymstudien II. Biochemische Zeitschrift (1909) 21, 131.

9 L. Michaelis and H. Davidsohn, Biochemische Zeitschrift (1911) 35, 386.

10 As in many places throughout the article, no units are given and we presume M, giving pH 4.7.

in all solutions, which is on the one hand the optimal H+-concentration for the activity of the enzyme and on the other hand the H+-concentration at which there is the lowest variation of enzyme activity as a result of a small random deviation from this concentration, since in the region of the optimal H+-concentration the dependence of the enzyme activity on the H+-concentration is extremely small.

At least as important in the work of Henri is the lack of consideration of the fact that on inversion of the sugar, glucose is formed initially in its birotational form and is only slowly converted to its normal rotational form.11) Monitoring the progress of the inversion reaction by direct continuous observation of the polarization angle therefore leads to a falsification of the true rate of inversion, since this is superimposed on the change in polarization of the freshly formed glucose. This could be allowed for by including the rate of glucose equilibration in the calculations. However, this is not realistic, since highly complex functions are generated which can be easily avoided experimentally. A better approach is to take samples of the inversion reaction mixture at known time intervals, to stop the invertase reaction and to wait until the normal rotation of glucose is reached before measuring the polarization angle. Sörensen used sublimate (HgCl2) while we used soda, which inactivates the invertase and removes the mutarotation of the sugar within a few minutes.12)

Incidentally, it should be noted that Hudson13) already adopted the approach of removing mutarotation experimentally using alkali, but came to a quite different conclusion to ours concerning the course of the invertase reaction. Thus, he is of the opinion that after removing the problem of mutarotation, inversion by invertase follows a simple logarithmic function similar to that of inversion by acid, but this result is contrary to all earlier investigations and according to our own work is not even correct to a first approximation. Even if Henri's experiments need to be improved, their faults are not as grave as Hudson believes. (Sörensen also noticed that Hudson's conclusions were incorrect). On the contrary, we are of the opinion that the basic considerations that started with Henri are indeed rational, and we will now attempt to use improved techniques to demonstrate this. It will become apparent that the basic tenets of Henri are, at least in principle, quite correct, and that the observations are now in better accord with them than are Henri's own experiments.

Henri has already shown that the cleavage products of sugar inversion, glucose and fructose, have an inhibitory effect on invertase action. Initially, we will not attempt to allow for this effect, but will choose experimental conditions which avoid this effect. Since the effect is not large, this is, in principle, simple. At varying starting concentrations of sucrose, we only need to follow the inversion reaction in a time range where the influence of the cleavage products is

11 The cleavage of sucrose initially gives the a-anomer (a-D-glucopyranose), which then equilibrates to a mixture of a- and ß-anomers (ca. 65% }); the meaning of birotational is not entirely clear.

12 This is not strictly correct since mutarotion describes the equilibration of the a and B anomers, which is not removed; rather, the treatment with alkali accelerates the equilibration.

3 C. S. Hudson, J. Amer. Chem. Soc. (1908) 30, 1160 and 1564; (1909) 31, 655; (1910) 32, 1220 and 1350 (1910).

not noticeable. Thus, we will initially only measure the starting velocity of inversion at varying sucrose concentrations. The influence of the cleavage products can then be easily observed in separate experiments.

## 1. The initial reaction velocity of inversion at varying sucrose concentrations

The influence of the sucrose concentration on enzymatic inversion was examined by all authors already cited and led to the following general conclusions. At certain intermediate sucrose concentrations the rate is hardly dependent on the starting amount of sugar. The rate is constant at constant enzyme concentration but is reduced at lower and also at higher sugar concentration14). Our own experiments were performed in the following manner. A varying quantity of a sucrose stock solution was mixed with 20 ccm of a mixture of equal parts of 1/5 M acetic acid, 1/5 M sodium acetate, a certain quantity of enzyme, and water to give a volume of 150 ccm. All solutions were prewarmed in a water bath at 25 ± <0.05° and held at this temperature during the reaction. The first sample was taken as soon as possible after mixing the solution, followed by further samples at appropriate intervals. Every sample of 25 ccm was transferred to a vessel containing 3 ccm of 1/2 M Soda to immediately stop the enzyme activity. The solution was examined polarimetrically after approximately 1/2 hour. The initial polarization angle was extrapolated from the first actual measurements. This extrapolation is certainly valid, since it was only over a few hundredths of a degree. Regular checks that the mutarotation was complete were made by repeated measurements 1/2 hour later. Every measurement recorded in the protocol is the average of 6 individual measurements, which only differed by a few hundredths of a degree. If we now plot the rotation as a function of time for a single experiment, we see that at the beginning of the process the rotation decreases linearly with time over a fairly long stretch. We define the initial velocity of the inversion as the decrease of rotation per unit time in the phase that can be regarded as linear. The experiments led to the following results:

14 Perhaps the authors were referring to substrate inhibition at high sucrose concentrations, which is evident in Figs. 2a and 4a, and explained on page 14 as possibly due to changes in the solvent at high concentrations (e.g., 34% sucrose).

In Tables I through IV we give the rotation angle relative to the real zero point of the polarimeter, corrected for the (very small) rotation of the enzyme solution.

_Table I (Fig. 1)_

| Time (t) in | Corrected | Change in | Initial |
| :---: | :---: | :---: | :---: |
| minutes | rotation | rotation x | concentration |
|  |  |  | of Sucrose |
| 1. |  |  | 0.333 M |
| 0 | [14.124] | 0 |  |
| 1 | 14.081 | 0.043 |  |
| 7 | 13.819 | 0.305 |  |
| 14 | 13.537 | 0.587 |  |
| 26 | 13.144 | 0.980 |  |
| 49 | 12.411 | 1.713 |  |
| 75 | 11.502 | 2.602 |  |
| 117 | 10.156 | 3.968 |  |
| 1052 | -4.129 | 18.253 |  |
| theor. endpoint |  | 18.57 |  |

| Time (t) in | Corrected | Change in | Initial |
| :---: | :---: | :---: | :---: |
| Minutes | rotation | rotation x | concentration |
|  |  |  | of Sacrose |
| 2. |  |  | 0.167 M |
| 0 | [7.123] | 0 |  |
| 1 | 7.706 | 0.047 |  |
| 8 | 6.749 | 0.374 |  |
| 16 | 6.528 | 0.595 |  |
| 28 | 6.109 | 1.014 |  |
| 52 | 5.272 | 1.851 |  |
| 82 | 4.316 | 2.807 |  |
| 103 | 3.592 | 3.531 |  |
| 24 Std. | -2.219 | 9.342 |  |
| theor. endpoint |  | 9.35 |  |

| 3a. |  |  | 0.0833 M |
| :---: | :---: | :---: | :---: |
| 0 | [3.485] | 0 |  |
| 2.5 | 3.440 | 0.045 |  |
| 12.5 | 3.262 | 0.223 |  |
| 49.5 | 1.880 | 1.605 |  |
| 90.0 | 0.865 | 2.620 |  |
| 125.0 | 0.340 | 3.145 |  |
| 151.0 | 0.010 | 3.496 |  |
| 208.0 | -0.617 | 4.102 |  |
| 267.0 | -0.815 | 4.300 |  |
| 24 Std | -0.998 | 4.483 |  |
| theor. endpoint |  | 4.560 |  |

| 3b. |  |  | 0.0833 M |
| :---: | :---: | :---: | :---: |
| 0 | 3.394 | 0 |  |
| 1 | 3.367 | 0.027 |  |
| 6 | 3.231 | 0.163 |  |
| 13 | 2.941 | 0.453 |  |
| 21 | 2.672 | 0.722 |  |
| 22 | 2.302 | 1.092 |  |
| 57 | 1.626 | 1.768 |  |
| 90 | 0.824 | 2.570 |  |
| 24 Std | -1.109 | 4.503 |  |
| theor. endpoint |  | 4.56 |  |

| 4. |  |  | 0.0416 M |
| :---: | :---: | :---: | :---: |
| 0 | [1.745] | 0 |  |
| 2.25 | 1.684 | 0.061 |  |
| 10.25 | 1.487 | 0.258 |  |
| 30.75 | 0.929 | 0.816 |  |
| 61.75 | 0.359 | 1.386 |  |
| 90.75 | 0.061 | 1.684 |  |
| 112.75 | -0.169 | 1.914 |  |
| 132.75 | -0.339 | 2.084 |  |
| 154.75 | -0.374 | 2.119 |  |
| 1497.0 | -0.444 | 2.189 |  |
| theor. endpoint |  | 2.247 |  |

| 5. |  |  | 0.0208 M |
| :---: | :---: | :---: | :---: |
| 0 | [0.906] | 0 |  |
| 1 | 0.881 | 0.025 |  |
| 6 | 0.729 | 0.177 |  |
| 17 | 0.512 | 0.394 |  |
| 27 | 0.369 | 0.537 |  |
| 38 | 0.179 | 0.727 |  |
| 62 | 0.029 | 0.877 |  |
| 95 | -0.117 | 1.023 |  |
| 1372 | -0.230 | 1.136 |  |
| 24 Std. | -0.272 | 1.178 |  |
| theor. endpoint |  | 1.190 |  |

| 6. |  |  | 0.0104 M |
| :---: | :---: | :---: | :---: |
| 0 | [0.480] | 0 |  |
| 0.5 | 0.472 | 0.012 |  |
| 5.5 | 0.396 | 0.084 |  |
| 11.0 | 0.329 | 0.151 |  |
| 19.0 | 0.224 | 0.251 |  |
| 35.0 | 0.127 | 0.353 |  |
| 75.0 | 0.021 | 0.459 |  |
| 117.0 | -0.059 | 0.539 |  |
| 149.0 | -0.114 | 0.594 |  |
| 24 Std. | -0.127 | 0.607 |  |
| theor. endpoint |  | [0.630] |  |

| 7. |  |  | 0.0052 M |
| :---: | :---: | :---: | :---: |
| 0 | [0.226] | 0 |  |
| 1 | 0.219 | 0.007 |  |
| 8 | 0.172 | 0.054 |  |
| 16 | 0.092 | 0.134 |  |
| 28 | 0.056 | 0.170 |  |
| 50 | -0.012 | 0.238 |  |
| 80 | -0.089 | 0.315 |  |
| 114 | -0.117 | 0.343 |  |
| 2960 | -0.104 | 0.330 |  |
|  | ----- | ----- |  |
|  | ----- | ----- |  |

![Image](https://storage.googleapis.com/chunkr-prod-bucket/84b768a3-ce8f-4a71-8245-8c88c8639b23/f1ded069-e7ec-4fb2-a7ea-5649281478c8/images/7ce842be-86d5-4b85-9bac-00a623c3e931.jpg?x-id=GetObject&response-content-disposition=inline&response-content-encoding=utf-8&response-content-type=image%2Fjpeg&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=GOOG1EBMQ2D33SPB3VQ4MMVJEKXWQFNK5WS57JRFVYUSD3ZCA76OC3B74IG7C%2F20250528%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20250528T033640Z&X-Amz-Expires=3600&X-Amz-SignedHeaders=host&X-Amz-Signature=2dba03a21a9e40441f9993550bb784ed6dad3fbf36e4e3562b3860b7396fe0fe)

_Fig. 1. Abscissa: Time in minutes. Ordinate: Decrease in rotation in degrees. Each curve is for an experiment with the given starting concentration of sucrose. The numbers of the experiments (1 to 7) correspond to those of Table I.15) Experiment 3 represents the combined results of the parallel experiments 3a and 3b. Amount of enzyme is the same in all experiments._

_Results of the experiment in Table I (Fig. 1a)_

| | Initial velocity | Initial Concentration of Sucrose <br> *a* | log *a* |
|---|---|---|---|
| 1. | 3.636 | 0.3330 | -0.478 |
| 2. | 3.636 | 0.1670 | -0.777 |
| 3. | 3.236 | 0.0833 | -1.079 |
| 4. | 2.666 | 0.0416 | -1.381 |
| 5. | 2.114 | 0.0208 | -1.682 |
| 6. | 1.466 | 0.0104 | -1.983 |
| 7. | 0.866 | 0.0052 | -2.284 |

15 The numbers on the figure define the experiment number and the molar concentration of sucrose.

_Fig 1a. Abscissa: Logarithm of initial concentration of sucrose. Ordinate: The initial rate of cleavage, expressed as the decrease of rotation (in degrees) per unit time (minutes), extracted graphically from Fig. 1. Concerning the "rational scale" of the ordinate, see pp. 12-13._

![Image](https://storage.googleapis.com/chunkr-prod-bucket/84b768a3-ce8f-4a71-8245-8c88c8639b23/f1ded069-e7ec-4fb2-a7ea-5649281478c8/images/5ba75018-f311-45df-adc9-53571a570c8f.jpg?x-id=GetObject&response-content-disposition=inline&response-content-encoding=utf-8&response-content-type=image%2Fjpeg&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=GOOG1EBMQ2D33SPB3VQ4MMVJEKXWQFNK5WS57JRFVYUSD3ZCA76OC3B74IG7C%2F20250528%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20250528T033640Z&X-Amz-Expires=3600&X-Amz-SignedHeaders=host&X-Amz-Signature=ed7932e8617efa90dd84ba2fcd3cc70811cd362202c4ff780dc38e26f3e916b0)

_Table II (Fig. 2)_

|   | Time (t) in minutes | Rotation | Change in rotation | Initial concentration of Sucrose | | Time (t) in minutes | Rotation | Change in rotation | Initial concentration of Sucrose |
|---|---|---|---|---|---|---|---|---|---|
| A | 0 | [31.427] | 0 | 0.77 M | B | 0 | [15.684] | 0 | 0.385 M |
|   | 0.5 | 31.393 | 0.034 |   |   | 0.5 | 15.643 | 0.041 |   |
|   | 7.0 | 30.951 | 0.476 |   |   | 7.0 | 15.148 | 0.536 |   |
|   | 15.0 | 30.486 | 0.941 |   |   | 15.0 | 14.543 | 1.141 |   |
|   | 23.0 | 30.025 | 1.402 |   |   | 23.0 | 13.935 | 1.749 |   |
|   | 38.0 | 29.185 | 2.242 |   |   | 38.0 | 13.183 | 2.501 |   |
| C | 0 | [7.949] | 0 | 0.192 M | D | 0 | [3.853] | 0 | 0.096 M |
|   | 0.5 | 7.910 | 0.039 |   |   | 0.5 | 3.810 | 0.043 |   |
|   | 7.0 | 7.407 | 0.542 |   |   | 9.0 | 3.090 | 0.763 |   |
|   | 15.0 | 6.790 | 1.159 |   |   | 17.0 | 2.741 | 1.112 |   |
|   | 23.0 | 6.161 | 1.788 |   |   | 25.0 | 2.063 | 1.790 |   |
|   | 32.0 | 5.523 | 2.426 |   |   | 34.0 | 1.551 | 2.302 |   |
| E | 0 | [2.063] | 0 | 0.048 M | F | 0 | [1.374] | 0 | 0.0308 M |
|   | 0.5 | 2.033 | 0.030 |   |   | 0.5 | 1.348 | 0.026 |   |
|   | 7.0 | 1.643 | 0.420 |   |   | 6.0 | 1.055 | 0.319 |   |
|   | 15.0 | 1.197 | 0.866 |   |   | 13.0 | 0.706 | 0.668 |   |
|   | 23.0 | 0.791 | 1.272 |   |   | 22.0 | 0.403 | 0.971 |   |
|   | 32.0 | 0.440 | 1.623 |   |   | 32.0 | 0.138 | 1.236 |   |
| G | 0 | [0.707] | 0 | 0.0154 M | H | 0 | [0.360] | 0 | 0.0077 M |
|   | 0.5 | 0.690 | 0.017 |   |   | 0.5 | 0.348 | 0.012 |   |
|   | 6.0 | 0.505 | 0.202 |   |   | 6.0 | 0.220 | 0.140 |   |
|   | 13.0 | 0.340 | 0.367 |   |   | 13.0 | 0.161 | 0.199 |   |
|   | 22.0 | 0.160 | 0.547 |   |   | 22.0 | 0.105 | 0.255 |   |
|   | 32.0 | 0.050 | 0.657 |   |   | 32.0 | 0.046 | 0.314 |   |

![Image](https://storage.googleapis.com/chunkr-prod-bucket/84b768a3-ce8f-4a71-8245-8c88c8639b23/f1ded069-e7ec-4fb2-a7ea-5649281478c8/images/9fe58469-226a-45de-b58b-8e2063a2270b.jpg?x-id=GetObject&response-content-disposition=inline&response-content-encoding=utf-8&response-content-type=image%2Fjpeg&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=GOOG1EBMQ2D33SPB3VQ4MMVJEKXWQFNK5WS57JRFVYUSD3ZCA76OC3B74IG7C%2F20250528%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20250528T033640Z&X-Amz-Expires=3600&X-Amz-SignedHeaders=host&X-Amz-Signature=f769be0e8859a0997e8670c30170693cb27a629fdebb37a39705b022dc654fad)

_Fig. 2. Terms as in Fig. 1. Graphical representation of the experiment in Table II. Approximately double the enzyme amount as in Fig. 1.16)_

_Results of the experiment in Table II (Fig. 2a)_

| | Initial velocity | Initial Concentration of Sucrose | log a |
|---|---|---|---|
| 1. | 0.0630 | 0.7700 | -0.114 |
| 2. | 0.0750 | 0.3850 | -0.414 |
| 3. | 0.0750 | 0.1920 | -0.716 |
| 4. | 0.0682 | 0.0960 | -1.017 |
| 5. | 0.0583 | 0.0480 | -1.318 |
| 6. | 0.0500 | 0.0308 | -1.517 |
| 7. | 0.0350 | 0.0154 | -1.813 |
| 8. | 0.0267 | 0.0077 | -2.114 |

16 The concentrations of sucrose in M are listed in Fig. 2 for each experiment (A-H) according to Table II.

![Image](https://storage.googleapis.com/chunkr-prod-bucket/84b768a3-ce8f-4a71-8245-8c88c8639b23/f1ded069-e7ec-4fb2-a7ea-5649281478c8/images/9192eff6-84b5-45d8-9ae0-385d354086b1.jpg?x-id=GetObject&response-content-disposition=inline&response-content-encoding=utf-8&response-content-type=image%2Fjpeg&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=GOOG1EBMQ2D33SPB3VQ4MMVJEKXWQFNK5WS57JRFVYUSD3ZCA76OC3B74IG7C%2F20250528%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20250528T033640Z&X-Amz-Expires=3600&X-Amz-SignedHeaders=host&X-Amz-Signature=efdc0473aee95ea8e85de5e70475cbb8d5e88a1193dd97e4386acc93def65efc)

_Fig 2a. The presentation corresponds to Fig. 1a; calculated from Fig. 2._

_Table III (Fig. 3)_

|   | Time (t) in minutes | Rotation | Change in rotation | Initial quantity of Sucrose | | Time (t) in minutes | Rotation | Change in rotation | Initial quantity of Sucrose |
|---|---|---|---|---|---|---|---|---|
| A | 0 | [30.946] | 0 | 0.77 M | B | 0 | [15.551] | 0 | 0.385 M |
|   | 0.5 | 30.935 | 0.011 |   |   | 0.5 | 15.541 | 0.010 |   |
|   | 30.0 | 30.325 | 0.621 |   |   | 30.0 | 14.973 | 0.578 |   |
|   | 60.0 | 29.715 | 1.231 |   |   | 60.0 | 14.353 | 1.198 |   |
|   | 90.0 | 29.286 | 1.660 |   |   | 90.0 | 13.810 | 1.741 |   |
|   | 123.0 | 28.506 | 2.440 |   |   | 123.0 | 13.138 | 2.413 |   |
|---|---|---|---|---|---|---|---|---|
| C | 0 | [7.623] | 0 | 0.193 M | D | 0 | [3.869] | 0 | 0.096 M |
|   | 0.5 | 7.613 | 0.010 |   |   | 0.5 | 3.860 | 0.009 |   |
|   | 31.0 | 6.990 | 0.633 |   |   | 27.0 | 3.366 | 0.503 |   |
|   | 55.0 | 6.430 | 1.193 |   |   | 53.0 | 2.791 | 1.078 |   |
|   | 74.0 | 6.040 | 1.583 |   |   | 74.0 | 2.533 | 1.336 |   |
|   | - | - | - |   |   | 101.0 | 1.998 | 1.871 |   |
|---|---|---|---|---|---|---|---|---|
| E | 0 | [2.004] | 0 | 0.048 M | F | 0 | [0.967] | 0 | 0.024 M |
|   | 0.5 | 1.995 | 0.009 |   |   | 0.5 | 0.953 | 0.004 |   |
|   | 27.0 | 1.485 | 0.546 |   |   | 27.0 | 0.711 | 0.246 |   |
|   | 53.0 | 1.113 | 0.891 |   |   | 53.0 | 0.446 | 0.511 |   |
|   | 74.0 | 0.848 | 1.156 |   |   | 73.0 | 0.343 | 0.614 |   |
|   | 101.0 | 0.555 | 1.449 |   |   | 100.0 | 0.195 | 0.762 |   |

_Results of the experiment in Table III (Fig. 3a) 17)_

| | Concentration (x) | log(x) | Initial velocity (v) |
|---|---|---|---|
| 1. | 0.770 | -0.114 | 0.3166 (0.02) |
| 2. | 0.385 | -0.414 | 0.3166 (0.02) |
| 3. | 0.193 | -0.716 | 0.2154 (0.0215) |
| 4. | 0.096 | -1.017 | 0.0192 |
| 5. | 0.048 | -1.318 | 0.0166 |
| 6. | 0.024 | -1.619 | 0.0088 (0.0135) |

17 Numbers in this table were inconsistent with Fig. 3a. To reproduce the figure, we used a micrometer to estimate the values from the graph, as indicated by the numbers in parenthesis in the table, which were used to recreate Fig. 3a.

![Image](https://storage.googleapis.com/chunkr-prod-bucket/84b768a3-ce8f-4a71-8245-8c88c8639b23/f1ded069-e7ec-4fb2-a7ea-5649281478c8/images/43f61e71-e6ad-4c99-8dbf-49cb15d01c42.jpg?x-id=GetObject&response-content-disposition=inline&response-content-encoding=utf-8&response-content-type=image%2Fjpeg&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=GOOG1EBMQ2D33SPB3VQ4MMVJEKXWQFNK5WS57JRFVYUSD3ZCA76OC3B74IG7C%2F20250528%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20250528T033640Z&X-Amz-Expires=3600&X-Amz-SignedHeaders=host&X-Amz-Signature=155b93564ae15288d8efa3dc361afc0c65d1b3ae5bc18906739d0b3834da96ab)

_Fig 3. Graphical representation of the experiment in Table III. Amount of enzyme about half as large as in Fig. 1._

![Image](https://storage.googleapis.com/chunkr-prod-bucket/84b768a3-ce8f-4a71-8245-8c88c8639b23/f1ded069-e7ec-4fb2-a7ea-5649281478c8/images/f04132ce-56f5-48f2-bfd1-8b340e5984e7.jpg?x-id=GetObject&response-content-disposition=inline&response-content-encoding=utf-8&response-content-type=image%2Fjpeg&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=GOOG1EBMQ2D33SPB3VQ4MMVJEKXWQFNK5WS57JRFVYUSD3ZCA76OC3B74IG7C%2F20250528%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20250528T033640Z&X-Amz-Expires=3600&X-Amz-SignedHeaders=host&X-Amz-Signature=5ed6d40c4b278bc95619aa9702762bd114ef6f3277c4e8ea9d014df1c8f1b81a)

_Fig 3a. Representation as Fig. 1a, calculated from Fig. 3. Table IV (Fig. 4)_

| Time (t) in | Rotation | Change in | Initial | Time (t) in | Rotation | Change in | Initial |
| --- | --- | --- | --- | --- | --- | --- | --- |
| minutes |  | rotation | quantity of Sucrose | minutes |  | rotation | quantity of Sucrose |
| 1. | | | | 2. | | | |
| 0 | [31.205] | 0 | 0.77 M | 0 | [15.588] | 0 | 0.385 M |
| 0.5 | 31.190 | 0.015 |  | 0.5 | 15.570 | 0.018 |  |
| 68.0 | 29.183 | 2.022 |  | 67.0 | 13.140 | 2.448 |  |
| 3. | | | | 4. | | | |
| 0 | [7.849] | 0 | 0.193 M | 0 | [3.980] | 0 | 0.096 M |
| 0.5 | 7.830 | 0.019 |  | 0.5 | 3.963 | 0.017 |  |
| 62.0 | 5.416 | 2.433 |  | 62.0 | 1.840 | 2.140 |  |
| 5. | | | | 6. | | | |
| 0 | [1.984] | 0 | 0.048 M | 0 | [1.031] | 0 | 0.024 M |
| 0.5 | 1.970 | 0.014 |  | 0.5 | 1.013 | 0.018 |  |
| 30.0 | 1.133 | 0.851 |  | 10.0 | 0.665 | 0.366 |  |
| - | - | - |  | 29.0 | 0.415 | 0.616 |  |
| - | - | - |  | 36.0 | 0.321 | 0.710 |  |

_Results of the experiment in Table IV (Fig. 4a)_

| | Concentration (x) | log x | Initial Velocity v |
|---|---|---|---|
| 1. | 0.770 | -0.114 | 0.0297 |
| 2. | 0.385 | -0.414 | 0.0365 |
| 3. | 0.193 | -0.716 | 0.0374 |
| 4. | 0.096 | -1.017 | 0.0345 |
| 5. | 0.048 | -1.318 | 0.0284 |
| 6. | 0.024 | -1.619 | 0.0207 |

To analyze these experiments, we assume with Henri that invertase forms a complex with sucrose that is very labile and decays to free enzyme, glucose and fructose. We will test whether such an assumption is valid on the basis of our experiments. If this assumption 3º is correct, the rate of inversion must be proportional to the prevailing concentration of the 0.193 sucrose-enzyme complex. 18)

If 1 mole of enzyme and 1 mole of sucrose form I mole of sugar-enzyme complex, the law of mass action requires that [S].[Q-q]=k·Q (1) where [S] is the concentration of free sucrose, or since only a vanishingly small fraction of it is bound by enzyme, the total concentration of sucrose; ¢ is the total molar enzyme concentration, q is the concentration of the complexed enzyme, [+-[] is the concentration of free enzyme, and k is the dissociation constant.

![Image](https://storage.googleapis.com/chunkr-prod-bucket/84b768a3-ce8f-4a71-8245-8c88c8639b23/f1ded069-e7ec-4fb2-a7ea-5649281478c8/images/97ebfc47-8272-49ba-9200-0ffdec82d151.jpg?x-id=GetObject&response-content-disposition=inline&response-content-encoding=utf-8&response-content-type=image%2Fjpeg&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=GOOG1EBMQ2D33SPB3VQ4MMVJEKXWQFNK5WS57JRFVYUSD3ZCA76OC3B74IG7C%2F20250528%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20250528T033640Z&X-Amz-Expires=3600&X-Amz-SignedHeaders=host&X-Amz-Signature=416aeaa1ca94133f874ad18f1c68db143e1e9fb4d695ac59cc878cbc77e0082c)

_Fig 4. Graphical representation of the experiment in Table IV. Enzyme amount approximately the same as in the experiment of Fig. 1._

18 The authors use the word "Verbindung", which is normally used these days for compound. English texts of the period use the expression "molecular compound" for the invertase:sucrose complex (A.J. Brown, J. Chem. Soc. Vol. 81, pp. 373-388, 1902).

![Image](https://storage.googleapis.com/chunkr-prod-bucket/84b768a3-ce8f-4a71-8245-8c88c8639b23/f1ded069-e7ec-4fb2-a7ea-5649281478c8/images/001d5a0a-4527-4dd2-833a-1aee85712cfa.jpg?x-id=GetObject&response-content-disposition=inline&response-content-encoding=utf-8&response-content-type=image%2Fjpeg&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=GOOG1EBMQ2D33SPB3VQ4MMVJEKXWQFNK5WS57JRFVYUSD3ZCA76OC3B74IG7C%2F20250528%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20250528T033640Z&X-Amz-Expires=3600&X-Amz-SignedHeaders=host&X-Amz-Signature=768c903d8e52a0804a2195877033e8f20dfc2a841d9128fac8c3fa65183a841a)

_Fig 4a. Representation as Fig. 1a. Calculated from the experiment of Fig. 4._

From this it follows that

Q=¢. _ [S] [S]+ k [S] [S]+ k must be v = C . D

This quantity proportional to the starting velocity, v, of the inversion reaction, therefore

v = C . D

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

. (3) . .

where C is the proportionality constant.19) Since we measure v in arbitrary units (change of rotation angle per minute), and since + is held constant in an experimental series, we can refer to V as V. Thus, V is a function that is C.¢ proportional to the true starting velocity, so that20)

V = [S] [S]+ k .

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

. . . . . . (4)

19 Equation 3 is the closest they come to the Michaelis-Menten equation. The constant C contains kcat and a factor to convert the change of optical rotation to concentration so that C.¢ is Vmax in units of optical rotation degrees per minute.

20 " In equation 4, V is actually a dimensionless number giving the fraction of maximum velocity, v/Vmax as we know it.

(2)

.

.

This function is formally the same as the association curve21) of an acid22)

[H+]+k [H+] p =

and in order to achieve a better graphical representation we will plot the logarithm of the independent variable on the abscissa. We can therefore plot V as a function of log[S] and should obtain the well known association curve. At this point, we do not know the true scale of the ordinate. We only know that the maximal value V =1 should be reached asymptotically and that the foot of the ordinate of value 1/2 should give the value of k. In order to find the scale, we use the following graphical procedure.

Let us assume that we have a number of points from the experiment that we assume should give an association curve. Since the scale of the points on the ordinate is arbitrary, we have to assume that it will be different from that of the abscissa. Setting s = log[S], the function that we wish to display graphically is

V = 10$ + k 10$

or, if we substitute 10 = e", where p (= 2.303) is the modulus of the decadic logarithm system,

V =~ eps eps + k

Differentiating, we obtain

dV p.k.eps ds (eps + k)2

This differential quotient defines the tangent of the slope of the specified part of the curve. The association curve has a region whose slope is especially easy to determine, since it is practically linear over an extended stretch. This is the middle of the curve, in particular around the region where the ordinate has a value of 1/2. We know (cf. the work just referenced) that this ordinate corresponds to the point log k on the abscissa. If we now substitute the value 1/2 for V and log(k) for s, i.e. k for e's, in the differential equation, we obtain

dV ds for V = 1/2

4 _P _2.3026 4 = 0.576

21 The term used was "Restdissoziationkurve", which we translate according to the meaning implied by the equation defining the fractional association of an acid versus pH. 22 L. Michaelis, Biochemische Zeitschrift 33, 182 (1911); see also, by the same author, The General Significance of the Hydrogen-Ion Concentration etc., in Oppenheimer's Handbook of Biochemistry, supplementary volume, 1913.

This means that the middle, almost linear part of the curve has a slope relative to the abscissa whose tangent is 0.576 (i.e. a slope of almost exactly 30°). This obviously only applies if the ordinate and the abscissa have the same scales. We now join the experimental points of the middle part of the curve by a straight line and find that the tangent of its slope has the value v.23) From this we can conclude that that the units of the abscissa are related to those of the ordinate in the ratio of 0.576:v, i.e. that the units of the ordinate are the v/0.576 of those of the abscissa. We can now calculate the proper scale of the ordinate. (cf. Fig. 1a, 2a, 3a, 4a; "rational scale"). We now determine the position of the point 0.5 on this new scale. The ordinate of the curve, which corresponds to this point, gives the value of log k at its foot on the abscissa. We now know the value of k and can construct the whole association curve point for point. We will do this to test whether all the observed points fit well to this curve, and in particular that the value of 1 is not exceeded. Doing this for our experiments, we determine a value for v for each curve; we then construct the curve according to this and find, with one exception to be discussed, a good agreement of the observed and calculated points.

A second method to determine the scale of the ordinate is the following. If several points at the right hand end of the curve are well determined, and if it is clear that the maximal value has been reached, we can rescale the ordinate to make this value equal to 1. Then we again construct the sloping middle part of the curve by joining the points with a straight line and determine which point corresponds to the ordinate 0.5 on the new scale. We now have all data to construct the curve.

The first method will be chosen if the middle part of the curve is well determined, the second if the points at the right hand end of the curve are determined more reliably. If possible, both methods are used to confirm the agreement of the values obtained; in case of slight disagreements, the average value is taken. Using a combination of these methods we were able to obtain all of the curves shown. In all 4 cases (curve 1a, 2a, 3a, 4a), a family of dissociation curves was constructed for all possible combinations of likely scales for the ordinate and the best fitting curve was selected by shifting to the right or the left until the observed experimental points gave the best fit. It is indeed possible to find curves in all cases that fit within the limits of the allowed tolerances, even though the 4 experimental series were performed with quite different amounts of enzyme.

The dissociation constant for the invertase-sucrose complex found in the individual experiments were:24)

|  | 1 | 2 | 3 | 4 |
|---|---|---|---|---|
| log k = | -1.78 | -1.78 | -1.80 | -1.78 |
| k = | 0.0167 | 0.0167 | 0.0160 | 0.0167 |

23 This is the Greek letter v, not be confused with the velocity, v.

24 The dissociation constant is given in units of M.

in good agreement, although experiments were carried out with different amounts of enzyme. We have here, for the first time, a picture of the magnitude of the affinity of an enzyme for its substrate and we measure the size of a "specific" affinity according to the van't Hoff definition of chemical affinity.

The meaning of this affinity constant is the following. If we could prepare the enzyme-sucrose complex in a pure form and were to dissolve it in water at a concentration such that the undissociated fraction was present at a concentration of 1 mol in 1 liter, there would be v0.0167 mol or 0.133 mol of free enzyme and the same amount of free sucrose in the solution.

The accuracy with which k can be determined is different in the 4 different experiments (Fig. 1a, 2a, 3a, 4a). To an inexperienced observer, the unavoidable arbitrariness in plotting the observed points will appear questionable. But in fact this has little influence. For example, the worst of our curves is arguably Fig. 3a. Here we find log k = 1.8. Perhaps we could draw an acceptable curve for log k = - 1.7 or -1.9. But assuming log k = - 2.0 would not be compatible with the shape of a dissociation curve, and the same applies for log k = - 1.5.25) Thus, the variance of the true value of k is not large, even for a curve as poor as in Fig. 3a, as long as we have shown in a number of better experiments that the curve can be regarded as an "association curve".

The agreement of the theoretical curve with the observed points is satisfactory from the lowest useable sucrose concentrations up to ca. 0.4 M (corresponding to a logarithmic value of ca. - 0.4). However, at higher concentrations there is a deviation such that the rate becomes slower rather than remaining constant.26) However, we are not concerned with this deviation, since in this situation we are not confronted with the pure properties of a dilute solution. It is to be expected that the developed quantitative relationships are only valid over a limited range. The reasons for the failure of the law at high sugar concentrations can be attributed to factors whose influence we cannot express quantitatively. The most important influence can be summarized as "change of the nature of the solvent". We cannot regard a 1 molar solution of sucrose, containing 34% sugar, simply as an aqueous solution, since the sugar itself changes the character of the solvent. This could lead to a change in the affinity constant between enzyme and sugar as well as the rate constant for the decay of the complex. As an example of the manner in which an affinity constant can change when the nature of the solvent changes on addition of an organic solvent, we can consider the investigation of Löwenherz") on the change in the dissociation constant of water on addition of alcohol. There is no change in the affinity up to 7% alcohol, but there is a progressive decrease as the concentration is increased further.

25 Theoretical dissociation curves can obviously be generated with log k = - 2.0 or -1.5 ; they mean the points are not well explained assuming these values of k.

26 The quantities of enzyme in the experimental series I, II, III, IV are calculated from the initial velocities to be almost exactly 1:2:0.5:1.

27 R. Löwenherz, Zeitschr. f. physikal. Chem. 20, 283 (1896) Biochemische Zeitschrift Band 42.

## 2. The influence of the cleavage products and other substances.

The cited authors, especially Henri, have already shown that the cleavage products glucose and fructose have an influence on the hydrolysis of sucrose. Henri found that the influence of fructose is greater than that of glucose. We now have the task of determining this influence in a quantitative manner. Like Henri, we assume that invertase has affinity not only for sucrose, but also for fructose and glucose, and we attempt to determine the values of the affinity constants. We did this in the following manner:

As before, the initial rate of hydrolysis of sucrose at a certain enzyme concentration is determined. In a second experiment, a known concentration of fructose or glucose is added and the initial rate of hydrolysis of sucrose is determined and compared. It is found that this is reduced. We can conclude from this that the concentration of the sucrose-enzyme complex is reduced in the second case, under the assumption that the initial rate is always an indicator of the complex. If vo and v are the initial velocities and Po and o the corresponding sucrose-enzyme complex concentrations, then

Vo : V = 90 : 9

If the concentration of enzyme, , partitions between the sucrose concentration S and the fructose concentration F, and if o is the concentration of the sucrose-enzyme complex and w that of the fructose-enzyme complex, it follows from the law of mass action that

S . (Φ - φ -ψ) = k · φ, F. (Φ - φ- ψ) = Κ. Ψ,

where k and ky are the respective affinity constants.

From these 2 equations, elimination of y leads to

k1 = S. 2-1 -k F.k Q

.

.

.

.

.

.

.

.

.

.

.

.

.

. (1)

Φ can be determined as follows: In a parallel experiment without ϕ fructose, the initial rate is v0 and the concentration of the sucrose-enzyme complex is (0; in the main experiment, these two are equal to v and o, respectively; therefore

V: V0 = Φ: Φο and q ==. 00 V

Vo S 90 = D. _ S+k

In the fructose-free experiment, according to equation (2) on p. 11

And therefore

S

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

. (2) . .

Q= S+k

VOS+k

.

.

.

.

.

.

.

.

.

.

.

.

or

¢ Vo S+k Q v S F.k ⎜ ⎝ in (1) = (S+k)

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

. (3)

# Accurate description of experiments on the inhibition by other substances (Fructose and Glucose)

_Table 5 (Fig. 5)_

| Time in minutes | Rotation | Change in rotation | Concentration |
|---|---|---|---|
| 1 | | | |
|  | 0.0 | [3.905] | 0.000 | Sucrose 0.1 M |
|  | 0.5 | 3.896 | 0.009 |  |
|  | 15.0 | 3.640 | 0.365 |  |
|  | 30.0 | 3.183 | 0.722 |  |
| I (repeats) | | | | |
|  | 0.0 | [3.926] | 0.000 | Sucrose 0.1 M |
|  | 0.5 | 3.915 | 0.011 |  |
|  | 30.0 | 3.223 | 0.703 |  |
|  | 46.0 | 2.971 | 0.935 |  |
| II | | | | |
|  | 0.0 | [5.643] | 0.000 | Sucrose 0.1 M |
|  | 0.5 | 5.633 | 0.010 | Glucose 0.1 M |
|  | 30.0 | 5.033 | 0.610 |  |
|  | 46.0 | 4.788 | 0.855 |  |
| III | | | | |
|  | 0.0 | [1.022] | 0.000 | Sucrose 0.1 M |
|  | 0.5 | 1.013 | 0.009 | Fructose 0.1 M |
|  | 30.0 | 0.468 | 0.554 |  |
|  | 46.0 | 0.237 | 0.785 |  |

![Image](https://storage.googleapis.com/chunkr-prod-bucket/84b768a3-ce8f-4a71-8245-8c88c8639b23/f1ded069-e7ec-4fb2-a7ea-5649281478c8/images/7cf2370f-2304-48c4-95f0-e62d33ef7694.jpg?x-id=GetObject&response-content-disposition=inline&response-content-encoding=utf-8&response-content-type=image%2Fjpeg&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=GOOG1EBMQ2D33SPB3VQ4MMVJEKXWQFNK5WS57JRFVYUSD3ZCA76OC3B74IG7C%2F20250528%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20250528T033640Z&X-Amz-Expires=3600&X-Amz-SignedHeaders=host&X-Amz-Signature=627e0554e68d6b900e6a1978aed3dada4ec3c59d405d8cf303040c28dc49f209)

_Fig 5. Graphical representation of the experiment in Table 5. Influence of glucose and fructose._

and finally by substitution

k1

Vo ¥0-1

⎟

V

.

.

.

.

.

_Table 6 (Fig. 6)_

| Time in minutes | Rotation | Change in rotation | Concentration |
|---|---|---|---|
| I | | | |
|  | 0.0 | [5.579] | 0.000 | Sucrose 0.133 M |
|  | 0.5 | 5.568 | 0.011 |  |
|  | 30.0 | 4.891 | 0.688 |  |
|  | 0.0 | [5.361] | 0.000 | Sucrose 0.133 M |
|  | 0.5 | 5.350 | 0.011 |  |
|  | 30.0 | 4.691 | 0.670 |  |
|  | 45.0 | 4.373 | 0.988 |  |
| II | | | |
|  | 0.0 | [7.678] | 0.000 | Sucrose 0.133 M <br> + Glucose 0.133 M |
|  | 0.5 | 7.665 | 0.013 |  |
|  | 30.0 | 7.080 | 0.598 |  |
|  | 0.0 | [7.595] | 0.000 | Sucrose 0.133 M <br> + Glucose 0.133 M |
|  | 0.5 | 7.585 | 0.010 |  |
|  | 30.0 | 6.971 | 0.624 |  |
|  | 45.0 | 6.735 | 0.860 |  |

![Image](https://storage.googleapis.com/chunkr-prod-bucket/84b768a3-ce8f-4a71-8245-8c88c8639b23/f1ded069-e7ec-4fb2-a7ea-5649281478c8/images/c3cb446a-57cb-4b82-b9ca-39dac61b0c23.jpg?x-id=GetObject&response-content-disposition=inline&response-content-encoding=utf-8&response-content-type=image%2Fjpeg&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=GOOG1EBMQ2D33SPB3VQ4MMVJEKXWQFNK5WS57JRFVYUSD3ZCA76OC3B74IG7C%2F20250528%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20250528T033640Z&X-Amz-Expires=3600&X-Amz-SignedHeaders=host&X-Amz-Signature=dac5e44b9518bc92d3ff33caa8ddc3c1ef16586aa9156ffe73d39426b935beaa)

_Fig. 6. Graphical representation of the experiment in Table 6. Influence of glucose._

_Table 7 (Fig. 7)_

| Time in minutes | Rotation | Change in rotation | Concentration |
|---|---|---|---|
| 0.0 | [3.384] | 0.000 | Sucrose 0.0833 M |
| 0.5 | 3.358 | 0.026 |  |
| 10.0 | 3.021 | 0.363 |  |
| 20.0 | 2.691 | 0.693 |  |
| 30.0 | 2.365 | 1.019 |  |
| 0.0 | [4.758] | 0.000 | Sucrose 0.0833 M <br> Glucose 0.0833 M |
| 5.0 | 4.736 | 0.022 |  |
| 10.0 | 4.453 | 0.305 |  |
| 20.0 | 4.190 | 0.568 |  |
| 30.0 | 3.950 | 0.808 |  |
| 0.0 | [0.885] | 0.000 | Sucrose 0.0833 M <br> Fructose 0.0833 M |
| 5.0 | 0.863 | 0.022 |  |
| 10.0 | 0.570 | 0.315 |  |
| 20.0 | 0.305 | 0.580 |  |
| 30.0 | 0.083 | 0.802 |  |

The protocol given describes the design of the experiment. As seen, the progress of cleavage is compared at optimal acidity and identical temperature in mixtures that are identical in terms of sucrose and enzyme but which differ in their content of fructose or glucose or in the absence of these substances. The nature of such experiments leads to certain limitations. The total concentration of sugars should not be 1º I so high that the character of the II III solvent is changed. In general, it is not advisable to use total concentrations of more than 0.3 M. 0.5° This necessitates the use of relatively low concentrations of sucrose. This means that the rate of conversion does not stay constant for long periods, so that the progress curve 0 deviates from linearity after small Fig. 7. Graphical representation of the 0 10 20 30 experiment in Table 7. I= Experiment with 0.0833 M sucrose II = Experiment with 0.0833 M sucrose + 0.0833 M glucose III = Experiment with 0.0833 M sucrose + 0.0833 M fructose Initial tangent is shown as a dashed line. changes in optical rotation, which leads to difficulties in estimating the initial rate unless graphical extrapolation procedures are used that are not free of arbitrariness. These deviations from linearity are often more pronounced with pure sucrose (e.g. Fig. 8, I) than in experiments with mixed sugars (Fig. 8, II), since the concentration of the inhibitory cleavage products changes relatively more strongly in the pure sucrose experiments than in experiments in which a certain amount of the inhibitory substance is present from the beginning of the experiment. The initial velocities needed for the calculations can only be obtained by graphical extrapolation: the actual curve is constructed by eye from the observed points and a tangent is estimated by eye to give the initial rate. This procedure cannot be regarded as highly accurate, but will suffice to give us a good idea of the size of the value we are interested in. The (geometrical) tangents are shown as dotted lines in Fig. 5. The value of the ratio of the trigonometrical tangents Tan I is

Tan II calculated from Fig. 5 to be 1.18; the value of = 1.29. Tan III Tan I

From this experiment we now know that -0 = 1.18 for glucose and 1.29 for fructose. Using formula (3) from p. 16 we can calculate that v

k glucose =4.8

Vo

k k sucrose and k fructose sucrose

=3.0

| Time in minutes | Rotation | Change in rotation | Concentration |
|---|---|---|---|
| I | | | |
| 0.0 | [1.728] | 0.000 | Sucrose 0.0416 M |
| 0.5 | 1.715 | 0.013 |  |
| 7.0 | 1.552 | 0.176 |  |
| 14.0 | 1.360 | 0.368 |  |
| 21.0 | 1.168 | 0.560 |  |
| 28.0 | 0.982 | 0.746 |  |
| 36.0 | 0.862 | 0.866 |  |
| 44.0 | 0.403 | 1.325 |  |
| II | | | |
| 0.0 | [-0.809] | 0.000 | Sucrose 0.0416 M <br> Fructose 0.0833 M |
| 1.0 | -0.831 | 0.022 |  |
| 7.0 | -0.961 | 0.152 |  |
| 15.0 | -1.116 | 0.307 |  |
| 22.0 | -1.238 | 0.429 |  |
| 32.0 | -1.471 | 0.662 |  |

Applying the same procedure to experiment (Fig. 7), we obtain

This is not a table. It is a mathematical equation.

Tang I / Tang II = 1.18 and Tang I / Tang III = 1.26

and therefore

k

= 4.6

=3.2

k glucose sucrose

k and k fructose sucrose

![Image](https://storage.googleapis.com/chunkr-prod-bucket/84b768a3-ce8f-4a71-8245-8c88c8639b23/f1ded069-e7ec-4fb2-a7ea-5649281478c8/images/3079ecad-0174-4809-991e-e71e33ec85ac.jpg?x-id=GetObject&response-content-disposition=inline&response-content-encoding=utf-8&response-content-type=image%2Fjpeg&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=GOOG1EBMQ2D33SPB3VQ4MMVJEKXWQFNK5WS57JRFVYUSD3ZCA76OC3B74IG7C%2F20250528%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20250528T033640Z&X-Amz-Expires=3600&X-Amz-SignedHeaders=host&X-Amz-Signature=11291b4b989fab56367aba1d60b6960fcbcf2cba91e03c2a2d1dfe637ea2728a)

_Fig. 8. Graphical representation of the experiment in Table 8. Influence of fructose._

From the experiment (Fig. 9) we obtain the following. Note, there is no deviation from a straight line in these experiments.

Tang I Tang II 1.27 and Tang I Tang III

=1.43

and therefore

k glucose =5.3 and k fructose =3.3

k sucrose

k

sucrose

_Table 9 (Fig. 9)_

| Time in minutes | Rotation | Change in rotation | Concentration |
|---|---|---|---|
| 1 | 0.0 [1.703] | 0.000 | Sucrose 0.0416 M |
|  | 0.5 | 1.698 | 0.015 |  |
|  | 7.0 | 1.501 | 0.212 |  |
|  | 14.0 | 1.335 | 0.378 |  |
|  | 21.0 | 1.153 | 0.560 |  |
| II | 0.0 [3.039] | 0.000 | Sucrose 0.0416 M |
|  | 0.5 | 3.031 | 0.008 | Glucose 0.0832 M |
|  | 7.0 | 2.923 | 0.116 |  |
|  | 14.0 | 2.745 | 0.294 |  |
|  | 21.0 | 2.608 | 0.431 |  |
| III | 0.0 [-0.834] | 0.000 | Sucrose 0.0416 M |
|  | 0.5 | -0.845 | 0.011 | Fructose 0.0832 M |
|  | 7.0 | -0.985 | 0.151 |  |
|  | 14.0 | -1.096 | 0.262 |  |
|  | 21.0 | -1.221 | 0.387 |  |

![Image](https://storage.googleapis.com/chunkr-prod-bucket/84b768a3-ce8f-4a71-8245-8c88c8639b23/f1ded069-e7ec-4fb2-a7ea-5649281478c8/images/d9bde434-6a87-4203-8390-bd54fbc2c326.jpg?x-id=GetObject&response-content-disposition=inline&response-content-encoding=utf-8&response-content-type=image%2Fjpeg&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=GOOG1EBMQ2D33SPB3VQ4MMVJEKXWQFNK5WS57JRFVYUSD3ZCA76OC3B74IG7C%2F20250528%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20250528T033640Z&X-Amz-Expires=3600&X-Amz-SignedHeaders=host&X-Amz-Signature=e108141db2d6336b76bb94aefecc7a58268c8c1ba5320b8106ca68b60cbc1b15)

_Fig. 9. Graphical representation of the experiment in Table 9. Influence of glucose and fructose._

For experiment (Fig. 6) we obtain

Tang I

Tang I Tang II =1.133 so that k glucose =6.7 k sucrose

k sucrose

For experiment (Fig. 8) we obtain

Tang I Tang II =1.33 so that k fructose =4.3 k sucrose

k sucrose

Summarizing these data, we have

|  |  |  |  | Average |
|---|---|---|---|---|
|  $\frac{k_{glucose}}{k_{sucrose}} = 4.7$ | 4.6 | 5.3 | 6.7 | 5.3 |
| $\frac{k_{fructose}}{k_{sucrose}} = 3.0$ | 3.2 | 3.3 | 4.3 | 3.45 |

Using (3), p. 16, this leads to the following values for the dissociation constants:

Glucose-invertase complex = 0.088 M Fructose-invertase complex = 0.058 M

The inhibitory influence of other substances was measured in the same manner. Before doing this, as a test for the correctness of the procedure described above, we had to show that foreign substances that were expected to have no affinity to invertase did not inhibit the cleavage of cane sugar as long as their concentration did not change the character of the solvent. We therefore convinced ourselves again that a 0.1 normal concentration of potassium chloride had

absolutely no inhibitory effect and that even a normal concentration had no significant effect (Tables 10 and 13).

_Table 10 28)_

| Time in minutes | Rotation | Change in rotation | Concentration |
|---|---|---|---|
| A 0.0 | [3.901] | 0.000 | Sucrose 0.1 M |
| 0.5 | 3.881 | 0.020 |  |
| 33.0 | 2.540 | 1.361 |  |
| 59.0 | 1.716 | 2.185 |  |
| B 0.0 | [3.878] | 0.000 | Sucrose 0.1 M <br> Calcium chloride 0.1 M |
| 0.5 | 3.858 | 0.020 |  |
| 33.0 | 2.561 | 1.317 |  |
| 59.0 | 1.693 | 2.185 |  |
| V 0.0 | [3.907] | 0.000 | Sucrose 0.1 M <br> Mannitol 0.1 M <br> (cf Table 14) |
| 0.5 | 3.885 | 0.020 |  |
| 33.0 | 2.573 | 1.334 (1.23) |  |
| 59.0 | 1.761 | 2.146 (1.95) |  |
| C 0.0 | [4.001] | 0.000 | Sucrose 0.1 M <br> + 1 M-Alcohol |
| 0.5 | 3.985 | 0.016 |  |
| 33.0 | 2.935 | 1.006 (1.07) |  |
| 59.0 | 2.141 | 1.860 |  |
| D 0.0 | [3.971] | 0.000 | Sucrose 0.1 M <br> + Alcohol 0.2 M |
| 0.5 | 3.951 | 0.020 |  |
| 33.0 | 2.601 | 1.370 |  |
| 59.0 | 1.868 | 2.103 |  |

![Image](https://storage.googleapis.com/chunkr-prod-bucket/84b768a3-ce8f-4a71-8245-8c88c8639b23/f1ded069-e7ec-4fb2-a7ea-5649281478c8/images/6d71a372-38e1-4c53-a34a-90304b2460e5.jpg?x-id=GetObject&response-content-disposition=inline&response-content-encoding=utf-8&response-content-type=image%2Fjpeg&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=GOOG1EBMQ2D33SPB3VQ4MMVJEKXWQFNK5WS57JRFVYUSD3ZCA76OC3B74IG7C%2F20250528%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20250528T033640Z&X-Amz-Expires=3600&X-Amz-SignedHeaders=host&X-Amz-Signature=19e17a2e53a25ce3b18933822da0095f082c00e0839ec6c5efdd03c5af6e1739)

_Fig. 10. Graphical representation of the experiment in Table 10. O · Trial A, B, D. V Trial V (Glycerin 0.1 M). ATrial C (Alcohol 1 M)._

At a concentration of 0.2 M, ethanol does not show the slightest inhibitory effect (Table 10). In contrast, there is a slight inhibition at normal concentration, which is without doubt due to a change in the character of the solvent and does not

28 There was a discrepancy between the numbers in Table 10 and Fig. 10. In order to reproduce Fig. 10, we measured values from the figure using a micrometer to get the numbers shown in parentheses and used these values to create Fig 10.

arise from an affinity of the enzyme to alcohol. If one wished to calculate the effect in terms of an affinity as done previously, graphical estimation of the ratio

k

alcohol k sucrose

would give a value of 36. Such a weak affinity can be equated to 0 within error limits (i.e. kalcohol = 00), especially when we bear in mind that another inhibitory factor, namely the change in character of the solvent, certainly plays a role.

The investigation of other carbohydrates or of poly-alcoholic substances was now of particular interest.

_Table 11._

| Time in minutes | Rotation | Change in rotation | Concentration |
|---|---|---|---|
| 0.0 | [2.081] | 0.000 | Sucrose 0.05 M |
| 0.5 | 2.065 | 0.016 |  |
| 20.0 | 1.386 | 0.695 |  |
| 50.0 | 0.548 | 1.533 |  |
| 0.0 | [5.373] | 0.000 | Sucrose 0.05 M <br> + 0.1 M-Lactose <br> (Milk sugar) |
| 0.5 | 5.358 | 0.015 |  |
| 20.0 | 4.750 | 0.628 |  |
| 50.0 | 3.815 | 1.558 |  |
| 0.0 | [8.805] | 0.000 | Sucrose 0.05 M <br> + 0.2 M-Lactose |
| 0.5 | 8.790 | 0.015 |  |
| 20.0 | 8.168 | 0.637 |  |
| 50.0 | 7.315 | 1.490 |  |

![Image](https://storage.googleapis.com/chunkr-prod-bucket/84b768a3-ce8f-4a71-8245-8c88c8639b23/f1ded069-e7ec-4fb2-a7ea-5649281478c8/images/be144d2d-3f06-45a5-9c08-44f81b0fd09e.jpg?x-id=GetObject&response-content-disposition=inline&response-content-encoding=utf-8&response-content-type=image%2Fjpeg&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=GOOG1EBMQ2D33SPB3VQ4MMVJEKXWQFNK5WS57JRFVYUSD3ZCA76OC3B74IG7C%2F20250528%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20250528T033640Z&X-Amz-Expires=3600&X-Amz-SignedHeaders=host&X-Amz-Signature=7749fa2a7e6ccf7dd1aa2b5f1ac61653a006f65c15fb450b2c00f81cc85144c3)

_Fig. 11. Graphical representation of the experiment in Table 11. Effect of lactose._

The behavior of milk sugar was of special interest (Tables 11 and Fig. 11). Its inhibitory influence was so slight, that it was hardly detectable inside the error limits. If we evaluated the very slight signal changes, we would find

|  | Experiment 1 | Experiment 2 |
|---|---|---|
| $\frac{k_{lactic}}{k}$ = | at least 30 | 36 |

k sucrose

Since we cannot say whether the small effects can be used reliably, we have to be satisfied with the statement that an affinity of milk sugar to invertase is not measurable with certainty. This is in agreement with our expectations, since binding of a disaccharide such as lactose to invertase would lead to hydrolysis, as is the case for sucrose, whereas lactose is not cleaved.

Mannose. An experiment gave (Tables 12 and Fig. 12)

k k sucrose

mannose =5.0

_Table 12._

| Time in minutes | Rotation | Change in rotation | Concentration |
|---|---|---|---|
| 0.0 | [3.901] | 0.000 | Sucrose 0.1 M |
| 0.5 | 3.881 | 0.020 |  |
| 33.0 | 2.540 | 1.361 |  |
| 59.0 | 1.716 | 2.185 |  |
| 0.0 | [4.717] | 0.000 | Sucrose 0.1 M <br> + Mannose 0.2 M |
| 0.5 | 4.703 | 0.014 |  |
| 33.0 | 3.778 | 0.939 |  |
| 59.0 | 2.887 | 1.830 |  |

For a more accurate determination, multiple repeated experiments would be needed. However, it can be seen that the affinity of mannose and glucose are similar.

![Image](https://storage.googleapis.com/chunkr-prod-bucket/84b768a3-ce8f-4a71-8245-8c88c8639b23/f1ded069-e7ec-4fb2-a7ea-5649281478c8/images/14d09a74-c4a6-4649-b8ac-e5d5f2124edb.jpg?x-id=GetObject&response-content-disposition=inline&response-content-encoding=utf-8&response-content-type=image%2Fjpeg&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=GOOG1EBMQ2D33SPB3VQ4MMVJEKXWQFNK5WS57JRFVYUSD3ZCA76OC3B74IG7C%2F20250528%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20250528T033640Z&X-Amz-Expires=3600&X-Amz-SignedHeaders=host&X-Amz-Signature=51a525d3cd83eecc7ba3dfda268291b4ca01c77adf2e45cd7fea3176dea6f21a)

_Fig. 12. Graphical representation of the experiment in Table 12. Effect of mannose._

## Mannitol

The inhibitory effect was low. This example was used to determine a weak affinity quantitatively by adequate variation of experimental conditions.

_Table 13_

| Time in minutes | Rotation | Change in rotation | Concentration |
|---|---|---|---|
| *I* | | | |
| 0.0 | [3.928] | 0.000 | Sucrose 0.1 M |
| 0.5 | 3.908 | 0.020 | |
| 33.0 | 2.610 | 1.318 | |
| 59.0 | 1.751 | 2.177 | |
| *IIa* | | | Sucrose 0.1 M <br> + Mannitol 0.1 M |
| 0.0 | [3.971] | 0.000 | |
| 0.5 | 3.953 | 0.018 | |
| 33.0 | 2.760 | 1.211 | |
| 59.0 | 1.747 | 2.224 | |
| *IIb* | | | Sucrose 0.1 M <br> + Mannitol 0.1 M |
| 0.0 | [3.907] | 0.000 | |
| 0.5 | 3.885 | 0.020 | |
| 33.0 | 2.573 | 1.334 | |
| 59.0 | 1.761 | 2.146 | |
| *III* | | | Sucrose 0.1 M <br> + Mannitol 0.25 M |
| 0.0 | [3.948] | 0.000 | |
| 0.5 | 3.930 | 0.018 | |
| 33.0 | 2.711 | 1.237 | |
| 59.0 | 1.938 | 2.010 | |
| *IV* | | | Sucrose 0.1 M <br> + Mannitol 0.5 M |
| 0.0 | [3.953] | 0.000 | |
| 0.5 | 3.938 | 0.015 | |
| 33.0 | 2.917 | 1.036 | |
| 59.0 | 2.205 | 1.748 | |
| *V* | | | Sucrose 0.1 M <br> + Mannitol 0.75 M |
| 0.0 | [3.921] | 0.000 | |
| 0.5 | 3.910 | 0.011 | |
| 33.0 | 3.163 | 0.758 | |
| 59.0 | 2.348 | 1.573 | |
|  | | | Sucrose 0.1 M <br> Calcium chloride 1 M |
| 0.0 | [3.952] | 0.000 | |
| 0.5 | 3.933 | 0.019 | |
| 33.0 | 2.700 | 1.252 | |
| 59.0 | 1.744 | 2.208 | |

_Table 14._

| Time in minutes | Rotation | Change in rotation | Concentration |
|---|---|---|---|
| 0.0 | [2.081] | 0.000 | Sucrose 0.05 M |
| 0.5 | 2.065 | 0.016 |  |
| 20.0 | 1.386 | 0.695 |  |
| 50.0 | 0.548 | 1.533 |  |
| VII<br>0.0 | [1.993] | 0.000 | Sucrose 0.05 M<br>+ Mannitol 0.2 M |
| 0.5 | 1.980 | 0.013 |  |
| 20.0 | 1.447 | 0.546 |  |
| 50.0 | 0.685 | 1.308 |  |
| VI<br>0.0 | [2.004] | 0.000 | Sucrose 0.05 M<br>+ Mannitol 0.1 M |
| 0.5 | 1.990 | 0.014 |  |
| 20.0 | 1.403 | 0.601 |  |
| 50.0 | 0.627 | 1.377 |  |

![Image](https://storage.googleapis.com/chunkr-prod-bucket/84b768a3-ce8f-4a71-8245-8c88c8639b23/f1ded069-e7ec-4fb2-a7ea-5649281478c8/images/16207d0c-f25f-464e-a914-72a246023ce3.jpg?x-id=GetObject&response-content-disposition=inline&response-content-encoding=utf-8&response-content-type=image%2Fjpeg&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=GOOG1EBMQ2D33SPB3VQ4MMVJEKXWQFNK5WS57JRFVYUSD3ZCA76OC3B74IG7C%2F20250528%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20250528T033640Z&X-Amz-Expires=3600&X-Amz-SignedHeaders=host&X-Amz-Signature=a96b44d8df96a8ab975f33493108fc90df52cbcf91a0e6ade5a4cdf32c835724)

_Fig. 13. (corresponding to Table 13) and Fig. 14 (corresponding to Table 14). Effect of mannose._

The following can be concluded from Table 13 and Fig. 13: The influence of 0.1 M mannitol on the cleavage of 0.1 M sucrose cannot be measured reliably. On increasing the amount of mannitol while keeping the amount of sucrose constant, the influence becomes gradually more obvious. From the procedure described above we obtain

| Experiment | III | IV | V | VI | VII |
|---|---|---|---|---|---|
| k<sub>maintained</sub>/k<sub>altered</sub> = | 17 | 13.4 | 10.5 | 11.4 | 11.4 |

Considering the small signals, the agreement is not bad, and the average value of

k k mannitol sucrose =13

should give a reasonable impression of the relative affinities.

Glycerin.

We have obtained the experimental series Fig. 15, Table 15 and an individual experiment (Fig. 10). We find

| Experiment | II | III | IV | V |
|---|---|---|---|---|
| $\frac{k_{glycerin}}{k_{water}} =$ | 3.4 | 5.6 | 3.9 | 5.1, with an average of 4.5. |

Thus, glycerin has, against expectations, a high affinity to invertase.

Summarizing the dissociation constants, we have: 29)

|             | k             | or |      |
|-------------|---------------|-----|------|
| Sucrose     | k = 0.0167    |     | 1/60 |
| Fructose    | k = 0.058     |  "  | 1/17 |
| Glucose     | k = 0.089     |  "  | 1/11 |
| Mannose     | k = ca. 0.083 |  "  | 1/12 |
| Glycerin    | k = ca. 0.075 |  "  | 1/13 |
| Mannitol    | k = 0.22      |  "  | 1/4.5|
| Lactose... at least | k = 0.5      |  "  | 1/2  |

(probably approaching o)

To help understand these values, it should be noted that an increase in the dissociation constant corresponds to a decrease of the affinity of the enzyme to the respective substance. Thus, the affinity of sucrose is by far the largest.

29 In units of M.

_Table 15._

| Time in minutes | Rotation | Change in rotation | Concentration |
|---|---|---|---|
| *I* 0.0 | [6.783] | 0.000 | Sucrose 0.166 M |
| 0.5 | 6.770 | 0.013 |  |
| 30.0 | 5.975 | 0.808 |  |
| *II* 0.0 | [6.652] | 0.000 | Sucrose 0.166 M |
| 0.5 | 6.646 | 0.006 |  |
| 60.0 | 5.470 | 1.182 |  |
| *II* 0.0 | [6.672] | 0.000 | Sucrose 0.166 M <br> + Glycerin 0.453 M |
| 1.0 | 6.650 | 0.022 |  |
| 30.5 | 6.008 | 0.664 |  |
| 49.0 | 5.690 | 0.982 |  |
| *III* 0.0 | [6.826] | 0.000 | Sucrose 0.166 M <br> + Glycerin 0.453 M |
| 0.5 | 6.813 | 0.013 |  |
| 30.0 | 6.013 | 0.813 |  |
| 49.0 | 5.961 | 0.865 |  |
| *IV* 0.0 | [6.789] | 0.000 | Sucrose 0.166 M <br> + Glycerin 0.906 M |
| 0.5 | 6.781 | 0.006 |  |
| 30.0 | 6.433 | 0.354 |  |
| 49.0 | 6.321 | 0.466 |  |

![Image](https://storage.googleapis.com/chunkr-prod-bucket/84b768a3-ce8f-4a71-8245-8c88c8639b23/f1ded069-e7ec-4fb2-a7ea-5649281478c8/images/2d18068a-bf4f-4131-aa12-5b31748fdc09.jpg?x-id=GetObject&response-content-disposition=inline&response-content-encoding=utf-8&response-content-type=image%2Fjpeg&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=GOOG1EBMQ2D33SPB3VQ4MMVJEKXWQFNK5WS57JRFVYUSD3ZCA76OC3B74IG7C%2F20250528%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20250528T033640Z&X-Amz-Expires=3600&X-Amz-SignedHeaders=host&X-Amz-Signature=2ee6b8c8c4c3b130934a52aca82c3108a2fadf5dc474c7099ba20fa4ce346758)

_Fig. 15. Graphical representation of the experiment in Table 15. Effect of glycerin. Experiment V is listed in Table 10._

The dissociation constant for the invertase-sugar complex is defined as

[enzyme]x[sugar]

[enzyme-sugar-complex]

so we can define the reciprocal value

[enzyme-sugar-complex] [enzyme]x[sugar]

as the affinity constant of the enzyme to the sugar. Thus we have:

| | |
|---|---|
| Sucrose | 60 |
| Fructose | 17 |
| Glucose | 11 |
| Mannose | ca. 12 |
| Glycerin | 13 |
| Mannitol | 4.5 |
| Lactose<br>Ethyl alcohol | 0 (i.e. immeasurably small) |

## 3. The reaction equation of the fermentative splitting of cane sugar.

On the basis of these data, we are now able to solve the old problem of the reaction equation of invertase in a real manner without resorting to the use of more than one arbitrary constant. Of all authors, V. Henri was closest to this solution, and we can regard our derivation as an extended modification of Henri's derivation on the basis of the newly gained knowledge.

The basic assumption in this derivation is that the decay rate at any instant is proportional to the concentration of the sucrose-invertase complex and that the concentration of this complex at any instant is determined by the concentration of enzyme, of sucrose and of reaction products that are able to bind to the enzyme. Whereas Henri introduced an "affinity constant for the cleavage products", we operate with the dissociation constant of the sucrose-enzyme complex, k = 1/60, with that of the fructose-enzyme complex, k= 1/17, and with that of the glucose- enzyme complex, k= 1/11.

We also use the following designations:

+= the total enzyme concentration

q= the concentration of the enzyme-sucrose complex

Y1 = the concentration of the enzyme-fructose complex

Y2 = the concentration of the enzyme-glucose complex S = the concentration of sucrose i.e. the concentration of the respective sugar

F = the concentration of fructose in the free state, which is practically equal to the total concentration.

G = the concentration of glucose

Since the cleavage yields equal amounts of fructose and glucose, G is always equal to F.

According to the law of mass action, at any instant

S.(+-0-V1-42)=k. F.(+-0-1-42)=k.41 G.(Ø-Q-¥1-V2)=K2·V2 S.(+-V1-42) S+k it follows that

From (1)

V2 =~· V1, k Kz k F k (1) by (3) to V1=K‘S'

and further by dividing give

V1=K‘S'

so that

V1+V2=K·Q| + |. F S 1 1

k k 1 2

)

For abbreviation we substitute

1 1

-+ == 9 k k, 2

so that

V1+V2=k.q.Q. F S

Substituting in (4), this gives

S

. . . (4) 30)

We can now proceed to the differential equation. If

a is the starting amount of sucrose

t is the time

x is the amount of fructose or glucose, so that

a-x is the remaining amount of sucrose at time t, the decay velocity at time t is defined by

0, = ax

30 Note the duplicate use of equation number (4).

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

. . . (4)

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

. . (2)

. .

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

. . (1)

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

.

φ=Φ. S+k.(1+q.F) .

dx dt

. . . (3)

We can eliminate \1 and \2 by first dividing (2) by (3) to give

.

According to our assumptions, this is proportional to o, so that the differential equation derived using equation (4) is:

dx

== C.

a- x (5)

dt a+k-x·(1-k·q)

where C is the only arbitrary constant, which is proportional to the amount of enzyme.31)

The general integral of the equation can be calculated without difficulty:

C.t=(1-k.q). x-k.(1+a.q). In(a-x)+const

To eliminate the integration constant, we substitute the values of x=0 and t=0 for the start of the process to give 32)

0 =- k . (1+ a . q) . Ina + const

and find by subtraction of the last two equations the definite integral

C.t = k . (1+a.q) . In --- +(1-k·q) . x (6)

or on substituting the value for q:

k 1 t a ⋅ ⎛ ⎜ ⎝ +

1 k

1 +

1 k ⎞ ⎠ · a · In

a a- x +

k

⋅

t

⎜ ⎛ ⎝ 1 k

− 1 k −

⎞ ⎠ . .

1 k, 2 x= C

We can now incorporate k into the constant on the right hand side of the equation and obtain

At1 1 x= const .. ) + a a-x + -. t 2 k 1 + k 1 k, 2

Like the Henri function, this is characterized by a superposition of a linear and a logarithmic function of the type

a

m . In-"+n . x =t . const a - x

(8)

where the meaning m and n can be seen by inspection of the previous equation: they are factors whose magnitude is dependent on the respective dissociation constants and starting quantity of the sugar.

31 This is not the C used in the earlier equations; rather, it includes the enzyme concentration and, as described below, a conversion from degrees of optical rotation to fractional conversion of substrate to product (x/a), so C = kcat Eo-

32 We corrected a sign error here that was not propagated to the next equation.

1 +

k 1

k, 2

a- x a

Substituting the determined values of k, k1 and k2 at 25° we obtain

1

· (1+ 28 . a) . 2.303 . log. 510 a

a-x t 1 + - . 32 . x = const. (9)

t

Instead of log-@ we use the simpler expression -log 1-2 a- x a

a

⎟

This constant must be proportional to the quantity of enzyme. That this is the case was shown by L. Michaelis and H. Davidsohn (l.c. p. 398-400), who demonstrated that an equation of the form

enzyme quantity x time = f(a,x) (10)

is strictly followed. The hitherto unknown function of the right hand side of the equation finds its definitive form in our equation (8). Otherwise nothing is changed and it can be easily seen that the constant in equation (8) must be proportional to the enzyme concentration.

While it is not necessary to test the correctness of equation (9) for varying amounts of enzyme, it still has to be tested whether the constant has the same value if the amount of enzyme is kept constant and the amount of sugar is varied, and whether the constant in a single experiment is independent of the time.

For these calculations, we use the data from experimental series I, and must first convert the values for x, for which we have so far used arbitrary polarimetric units, into concentration units. To do this we use the observation that the theoretical rotation of a sucrose solution which originally shows a rotation of mº is -0.313 x mº after complete cleavage of the sugar (cf. Sörensen, l.c., p. 262).

| Time (t) | x/a | const<sup><sup>3</sup>/<sub><sup>2</sup></sub></sup> | Average |
|---|---|---|---|
| **I. Sucrose 0.333 M** |  |  |  |
| 7 | 0.0164 | 0.0496 |  |
| 14 | 0.0316 | 0.0479 |  |
| 26 | 0.0528 | 0.0432 |  |
| 49 | 0.0923 | 0.0412 |  |
| 75 | 0.1404 | 0.0408 |  |
| 117 | 0.2137 | 0.0407 |  |
| 1052 | 0.9834 | [0.0498] | 0.0439 |
| **II. Sucrose 0.1667 M** |  |  |  |
| 8 | 0.0350 | 0.0444 |  |
| 16 | 0.0636 | 0.0446 |  |
| 28 | 0.1080 | 0.0437 |  |
| 52 | 0.1980 | 0.0444 |  |
| 82 | 0.3000 | 0.0445 |  |
| 103 | 0.3780 | 0.0454 | 0.0445 |
| **III. Sucrose 0.0833 M** |  |  |  |
| 49.5 | 0.352 | 0.0482 |  |
| 90.0 | 0.575 | 0.0447 |  |
| 125.0 | 0.690 | 0.0460 |  |
| 151.0 | 0.766 | 0.0456 |  |
| 208.0 | 0.900 | 0.0486 | 0.0465 |
| **IV. Sucrose 0.0416 M** |  |  |  |
| 10.25 | 0.1147 | 0.0406 |  |
| 30.75 | 0.3722 | 0.0489 |  |
| 61.75 | 0.615 | 0.0467 |  |
| 90.75 | 0.747 | 0.0438 |  |
| 112.70 | 0.850 | 0.0465 |  |
| 132.70 | 0.925 | 0.0443 |  |
| 154.70 | 0.940 | 0.0405 |  |
| 1497.00 | 0.972 | [0.0514] | 0.0445 |
| **V. Sucrose 0.0208 M** |  |  |  |
| 17 | 0.331 | 0.0510 |  |
| 27 | 0.452 | 0.0464 |  |
| 88 | 0.611 | 0.0500 |  |
| 62 | 0.736 | 0.0419 |  |
| 95 | 0.860 | [0.0388] |  |
| 1372 | 0.990 | [0.058] | 0.0474 |

_Average of all average values: 0.0454_

The value of the constant is very similar in all experiments and despite small variation shows no tendency for systematic deviation neither with time nor with sugar concentration, so that we can conclude that we can conclude that the value is reliably constant.

33 The term, const = Eo.kcat/Km, which would define the specificity constant if the enzyme concentration were known. In this table, Michaelis and Menten to calculate an average value, representing a global fit to their full time course data including product inhibition.

## Summary

The progress of invertase action is understandable based on the following assumptions:

Sucrose binds to invertase to give a complex with a dissociation constant of 0.0167.

This complex is unstable as a consequence of the equation

1 Mol sucrose-invertase-complex + I Mol fructose + 1 Mol glucose + 1Mol invertase

Invertase has an affinity to the cleavage products, fructose and glucose, as well as to several other higher alcohols (mannitol, glycerin) and carbohydrates (remarkably not to milk sugar), but this affinity is much lower than to sucrose. Since these complexes are not labile,34) they do not lead to a chemical cleavage reaction, but manifest themselves only in the inhibitory action of fructose etc. on the sucrose-invertase-process.

The concentration of all these complexes can be calculated according to the law of mass action and the dissociation constant for each complex can be given fairly accurately, most accurately for the sucrose-invertase-complex.

Since the decay of the sucrose-invertase-complex must be a monomolecular reaction, the respective decay rate of the sucrose is directly proportional to the concentration of the sucrose-invertase-complex.

Based on all these assumptions, a differential equation for the progress of the sucrose cleavage can be derived, whose integral is in good agreement with observations.

34 The authors mean the complexes of invertase formed with other sugars are not labile in terms of cleavage of chemical bonds.