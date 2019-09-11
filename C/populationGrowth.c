/* https://www.codewars.com/kata/563b662a59afc2b5120000c6 */

int nbYear(int p0, double percent, int aug, int p) {
    int yearcount = 0;
    while(p0 < p){
        p0 = p0 + (p0 * (percent / 100)) + aug;
        yearcount++;
    }
    return yearcount;
}
